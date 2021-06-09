import os.path as op
import numpy as np

class Config:
    class Paths:
        RESULT_ROOT = "/home/milab/machine_ws/Study/Dataset"
        TFRECORD = op.join(RESULT_ROOT, "tfrecord_homework3")
        
    class Tfrdata:
        DATASETS_FOR_TFRECORD = {"kitti": {"train", "val"}}
        MAX_BBOX_PER_IMAGE = 20
        CATEGORY_NAMES = ["Person", "Car", "Van", "Bicycle"]
        SHARD_SIZE = 2000
        ANCHORS_PIXEL = None

    class Train:
        BATCH_SIZE = 2