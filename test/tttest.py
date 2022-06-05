import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import sys
from layers import nms,iou
import cv2
# 'C:\\Users\\s4548361\\Desktop\\DSB2017_lbb.npy'
# shortname = '1.3.6.1.4.1.14519.5.2.1.6279.6001.100621383016233746780170740405'
shortname = '100158_3_1'
# label = np.load('work/black/pos/' + shortname + '_label.npy', allow_pickle=True)
img = np.load('bbox_result/' + shortname + '_lbb.npy')
pbb = np.load('bbox_result/' + shortname + '_pbb.npy')
pbb = pbb[pbb[:,0]>-1]
pbb = nms(pbb,0.05)
box = pbb[0].astype('int')[1:]

ax = plt.subplot(1,1,1)
plt.imshow(img[0,box[0]],'gray')
plt.axis('off')
rect = patches.Rectangle((box[2]-box[3],box[1]-box[3]),box[3]*2,box[3]*2,linewidth=2,edgecolor='red',facecolor='none')
ax.add_patch(rect)
plt.show()

# # img = np.load('bbox_result/' + shortname + '_same.npy')
# box = pbb[0].astype('int')[1:]
# slice = img[0, box[0]]
# patch = slice[box[1]-box[3]:box[1]+box[3], box[2]-box[3]:box[2]+box[3]]
# resized_patch = cv2.resize(patch, (32,32), interpolation = cv2.INTER_CUBIC)
# plt.imshow(resized_patch)
# plt.show()
# np.save('patch_1.npy', resized_patch)

box = pbb[0].astype('int')[1:]
slice = img[0, box[0]]
patch = slice[box[1]-16:box[1]+16, box[2]-16:box[2]+16]
resized_patch = cv2.resize(patch, (32,32), interpolation = cv2.INTER_CUBIC)
plt.imshow(resized_patch)
plt.show()
np.save('patch_1.npy', resized_patch)

for i in range(3):
    box = pbb[i].astype('int')[1:]
    slice = img[0, box[0]]
    patch = slice[box[1] - 16:box[1] + 16, box[2] - 16:box[2] + 16]
    resized_patch = cv2.resize(patch, (32, 32), interpolation=cv2.INTER_CUBIC)
    plt.imshow(resized_patch)
    plt.show()
    np.save('patch_'+str(i)+'.npy', resized_patch)