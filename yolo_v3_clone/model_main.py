from tfrecord.tfrecord_reader import TfrecordReader
from config import Config as cfg
import os.path as op

def main(data_name, split, batch_size):
    tfrpath = op.join(cfg.Paths.TFRECORD, f"{data_name}_{split}")
    reader = TfrecordReader(tfrpath, batch_size, 1)

if __name__ == "__main__":
    main("kitti", "train", cfg.Train.BATCH_SIZE)