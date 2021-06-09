import os.path as op
import json
import tensorflow as tf
import cv2

from config import Config as cfg   


class TfrecordReader:
    def __init__(self, tfrpath, shuffle=False, batch_size = cfg.Train.BATCH_SIZE,  epochs=1):
        self.tfrpath = tfrpath
        self.shuffle = shuffle
        self.batch_size = batch_size
        self.epochs = epochs
        self.config = self.read_tfrecord_config(tfrpath)
        self.features_dict = self.get_features(self.config)

    def read_tfrecord_config(self, tfrpath):
        with open(op.join(tfrpath, "tfr_config.txt"), "r") as fr:
            config = json.load(fr)
            print(config)
            for key, properties in config.items():
                if not isinstance(properties, dict):
                    continue
                properties["parse_type"] = eval(properties["parse_type"])
                properties["decode_type"] = eval(properties["decode_type"])
                # print(properties)
        return config

    def get_features(self, config):
        features_dict = {}
        for key, properties in config.items():
            if isinstance(properties, dict):
                default = "" if properties["parse_type"] is tf.string else 0
                features_dict[key] = tf.io.FixedLenFeature((), properties["parse_type"], default_value=default)
                print(features_dict)
