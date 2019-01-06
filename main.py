#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: CHEN Shen

import os
from preprocessing.datasets import VocLikeDataset
from encoder import DataEncoder
import config as cfg
from utils import get_mean_and_std
import preprocessing.transforms as transforms


if __name__ == '__main__':
    # cmd = "python2 test.py -m demo --backbone resnet101"
    # cmd = "python2 test.py -m valid --backbone resnet101"
    cmd = "python2 train.py --exp model -r"
    os.system(cmd)