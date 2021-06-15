# -*- coding: utf-8 -*-

import tensorflow as tf
# from IPython.display import SVG
# from tensorflow.python.keras.utils.vis_utils import model_to_dot
# %matplotlib inline
print(tf.version.VERSION)
print(tf.config.list_physical_devices('GPU'))


def myCNN(n_class, input_res=(32, 32, 3), output_channel=512): # 글자 목록 / 입력 해상도 / 출력 채널
    output_channel = [int(output_channel)/8, int(output_channel)/4, int(output_channel)/2, int(output_channel)]

    '''
    Dense - 모든 퍼셉트론 연결
    2D Convolution Layer - 2차원 합성곱 레이어
    2D MaxPooling - 최댓값을 기준으로하는 다운샘플링
    Relu Function - Sigmoid 진화형 (이지만 함수 특성상 음수에서 뉴런이 죽는 상황 발생하기도 함)
    SoftMax Fuction - 다중클래스 분류용 (각 요소의 편차에 대한 최적화)
    Batch Nomalization - 배치 정규화, weight 값에 정규화작업을 해준다. 배치의 크기가 적절해야한다.
    '''

    '''
    학습시간 단축을 위해서 레이어를 조금 줄여볼까 생각했는데, 그러다가는 정확도랑 내 손모가지가 같이 날라갈 것 같아서 배치정규화 조금 더 추가한 정도...?
    아직 능지가 부족하기 때문에 2048로 가는 길에서 급격하게 다운샘플 시키면 아무래도 신경망에 좋지는 않겠지..
    '''

    inputs = tf.keras.layers.Input(input_res)
    outputs = tf.keras.layers.Conv2D(output_channel[0], 3, padding='same', activation='relu')(inputs) # 32x32x64
    outputs = tf.keras.layers.MaxPooling2D(2, 2)(outputs) # 16x16x64
    outputs = tf.keras.layers.Conv2D(output_channel[1], 3, padding='same', activation='relu')(outputs) # 16x16x128
    outputs = tf.keras.layers.MaxPooling2D(2, 2)(outputs) # 8x8x128
    outputs = tf.keras.layers.Conv2D(output_channel[2], 3, padding='same', activation='relu')(outputs) # 8x8x256
    outputs = tf.keras.layers.Conv2D(output_channel[2], 3, padding='same', activation='relu')(outputs) # 8x8x256
    outputs = tf.keras.layers.BatchNormalization()(outputs) # [Add] 요정도까지는 배치정규화 시켜도 괜찮지 않을까.. 해서.. 나의 시간은 소중하기 때문에.....
    outputs = tf.keras.layers.ReLU()(outputs) # [Add]
    outputs = tf.keras.layers.MaxPooling2D(2, 2)(outputs) # 4x4x256
    outputs = tf.keras.layers.Conv2D(output_channel[3], 3, padding='same', activation='relu', use_bias=False)(outputs) # 4x4x512
    outputs = tf.keras.layers.BatchNormalization()(outputs)
    outputs = tf.keras.layers.ReLU()(outputs)
    outputs = tf.keras.layers.Conv2D(output_channel[3], 3, padding='same', activation='relu', use_bias=False)(outputs) # 4x4x512
    outputs = tf.keras.layers.BatchNormalization()(outputs)
    outputs = tf.keras.layers.ReLU()(outputs)
    outputs = tf.keras.layers.MaxPooling2D(2, 2)(outputs) # 2x2x512
    outputs = tf.keras.layers.Flatten()(outputs) # 2048 -> 현대한글의 글자수는 2350개
    outputs = tf.keras.layers.Dropout(0.3)(outputs)
    outputs = tf.keras.layers.Dense(n_class, activation='softmax')(outputs)

    return tf.keras.models.Model(inputs=inputs, outputs=outputs)


# SVG(model_to_dot(myCNN(2350), show_shapes=True).create(prog='dot', format='svg'))