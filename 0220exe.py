# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from skimage import io,util
import numpy as np
import matplotlib.pyplot as plt

ichan = io.imread('pic.png')

ichan_grey = io.imread('pic.png',as_grey=True) #copy and rename #True is 0~1 read as grey
ichan_grey = util.img_as_ubyte(ichan_grey)#set original png to grey #convert from 0_1 to 0_255

io.imshow(ichan)
plt.figure()

io.imshow(ichan_grey)

io.show() #show with cmd

print(ichan.shape)