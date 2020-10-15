import numpy as np
import pyvirtualcam
import argparse
import cv2
import sys
import os
import mxnet as mx
import datetime
from skimage import transform as trans
import insightface
import configparser
from utils.model_implementation import *
from utils.triangulation_implementation import *

handler = Handler('./../new_model/2d106det', 0, ctx_id=-1,
                  det_size=120)  # чем меньше размер картинки тем быстрее инференс, но точность ниже, норм при 120..

img1 = cv2.imread('../images/ava.png')
img1 = cv2.resize(img1, (640, 480))

preds_source = handler.get(img1, get_all=False)

print(img1.shape)
points1 = []
font = cv2.FONT_HERSHEY_SIMPLEX

# org
org = (50, 50)

# fontScale
fontScale = 0.3

# Blue color in BGR
color = (0, 0, 255)

# Line thickness of 2 px
thickness = 1
for pred in preds_source:
    pred = np.round(pred).astype(np.int)
    for i in range(pred.shape[0]):
        p = tuple(pred[i])
        points1.append(p)
        cv2.circle(img1, p, 1, (1, 0, 0))
        cv2.putText(img1, str(i), p, font, fontScale, color, thickness, cv2.LINE_AA)

cv2.imshow('123', img1)
cv2.imwrite('points.png', img1)
cv2.waitKey(1)
if cv2.waitKey(1) & 0xFF == ord('q'):
    pass