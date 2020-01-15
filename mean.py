import os
import numpy as np 
import matplotlib.pyplot as plt 
import PIL.Image as Image


path = './71/cropped/'
imgs = []
for name in os.listdir(path):
	img = Image.open(path + name)
	imgs.append(np.array(img))
imgs = np.stack(imgs, axis=0)
mean = imgs.mean(axis=0).astype(np.uint8)
img = Image.fromarray(mean)
img.save('mean.png')