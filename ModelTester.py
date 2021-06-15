# -*- coding: utf-8 -*-

import tensorflow as tf
import argparse
from Model import myCNN
from DatasetBuilder import DatasetBuilder


def evaluate(option):
    test_data_generate = DatasetBuilder(option.test_data, option, False)
