# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 14:04:25 2017

@author: tkustaff
"""

from skimage import io,util
#import numpy as np #array counting
import matplotlib.pyplot as plt

ichan = io.imread('pic.png')

ichan_grey = io.imread('pic.png',as_grey=True) #copy and rename #True is 0~1 read as grey
ichan_grey = util.img_as_ubyte(ichan_grey)

inverse = 255 - ichan
inverse2 = 255 - ichan_grey

io.imshow(inverse)
plt.figure()

io.imshow(inverse2)
