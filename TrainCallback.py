# -*- coding: utf-8 -*-

import tensorflow as tf
import tensorboard as tb
import os
import json

'''
트레인 돌면서 매 epoch 마다 현재 정보 알려주는 콜백..
인데 이거 있으면 더 느려지지 않을까 하는 생각이 문득..?이 아니라 에포크 까짓것 10번 이하로 하기 때문에 문제 없을듯
수치 표기의 경우에는 참고자료 그대로 이용했습니다. 다만 설명문은 영어에서 한국어로 바꿔서... 
'''

class TrainInfoIndicator(tf.keras.callbacks.Callback):
    def __init__(self, option):
        self.option = option
        self.max_acc = -1
        self.min_loss = 100000

    def on_epoch_end(self, epoch, logs=None):
        if logs is None: logs = {}
        val_acc = logs.get('val_acc')
        val_loss = logs.get('val_loss')

        if os.path.isdir(self.option.save_path) == False:
            os.mkdir(self.option.save_path)

        self.model.save_weights(os.path.join(self.option.save_path, f'{epoch + 1}_epoch_model.h5'))

        if val_acc is not None:
            if val_acc > self.max_acc:
                print('\n--- 가장 정확도가 높은 모델을 저장합니다 ---')
                self.max_acc = val_acc
                self.model.save_weights(
                    os.path.join(self.option.save_path, f'best_acc_{logs.get("val_acc"):.2f}_model.h5'))

            if logs.get('val_acc') >= 0.99:
                print('(!) 99%의 정확도를 달성했습니다')

        if val_loss is not None:
            if val_loss < self.min_loss:
                print('\n--- 가장 좋은 손실모델 가중치를 저장합니다 ---')
                self.min_loss = val_loss
                self.model.save_weights(
                    os.path.join(self.option.save_path, f'best_loss_{logs.get("val_loss"):.2f}_model.h5'))

