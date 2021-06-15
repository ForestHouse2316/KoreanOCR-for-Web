# -*- coding: utf-8 -*-

import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
import argparse
import random
import PIL

class DatasetBuilder(tf.keras.utils.Sequence):
    def __init__(self, path, labels, option, shuffle = True):
        self.path = path
        self.labels = labels
        print(path)

        self.n_samples = len(self.path) # 자료 수
        self.shuffle = shuffle # 뒤섞뒤섞
        self.train = True # 데이터셋 빌드 하자마자 바~로 학습 ㄱ
        self.batch_size = option.batch_size
        self.n_class = option.n_class
        self.idx_to_char = list(option.character) # 2350 자 String
        self.char_to_idx = {} # index_to_char 의 역 (딕셔너리 형태)
        for i, char in enumerate(self.idx_to_char): # enumerate : 리스트에 튜플 형식으로 인덱싱을 해줌. start 파라미터를 통해 시작값 커스터마이징 가능
            self.char_to_idx[char] = i

        self.n_class = len(self.idx_to_char) # 클래스 수
        self.n_samples = len(self.path) # 샘플 수

        self.indices = None # just declaring in __init__

        self.on_epoch_end()
        print(f'{self.n_samples} epoch end')

    def __len__(self):
        return int(np.floor(self.n_samples / self.batch_size))

    def on_epoch_end(self):
        self.indices = np.arange(self.n_samples)
        if self.shuffle:
            np.random.shuffle(self.indices)

    def __getitem__(self, index):
        indices = self.indices[index * self.batch_size:(index + 1) * self.batch_size]
        files = [self.path[i] for i in indices]
        labels = [self.labels[i] for i in indices]
        xs = []
        ys = []

        for file, label in zip(files, labels):
            x = load_img(file, target_size=(32, 32))
            x = img_to_array(x)
            x = x / 255.
            xs.append(x)

            ys.append(self.char_to_idx[label])

        return np.array(xs), np.array(ys)


'''
TestDataGenerator 의 경우 규격을 test.py랑 맞춰놓으셔서 수정이 어려워서 그냥 가져왔습니다...
개인적으로는 AI Hub 데이터만 쓰고 싶다만
'''

class TestDataGenerator(tf.keras.utils.Sequence):
    def __init__(self, data_path, opt, shuffle=True, train=True):
        self.path = data_path
        self.file_names = os.listdir(data_path)
        self.n_samples = len(self.file_names)
        # random.shuffle(self.file_names)
        self.shuffle = shuffle
        self.train = train
        self.indices = None

        self.batch_size = opt.batch_size
        self.num_class = len(opt.character)

        self.idx_to_char = list(opt.character)
        self.char_to_idx = {}
        for i, char in enumerate(self.idx_to_char):
            self.char_to_idx[char] = i

        self.on_epoch_end()
        print(f'{self.n_samples} images loaded')

    def __len__(self):
        return int(np.floor(self.n_samples / self.batch_size))

    def on_epoch_end(self):
        self.indices = np.arange(self.n_samples)
        if self.shuffle:
            np.random.shuffle(self.indices)

    def __getitem__(self, index):
        indices = self.indices[index * self.batch_size:(index + 1) * self.batch_size]
        files = [self.file_names[i] for i in indices]  # range(index*self.batch_size, (index+1)*self.batch_size)]
        xs = []
        ys = []

        for file in files:
            x = load_img(os.path.join(self.path, file), target_size=(32, 32))
            x = img_to_array(x)
            x = x / 255.
            xs.append(x)

            if self.train:
                label = file[0]
                ys.append(self.char_to_idx[label])

        return np.array(xs), np.array(ys)