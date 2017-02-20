# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from skimage import io #import image analyzing ability
import numpy as np
import matplotlib.pyplot as plt
import math
pic = io.imread("pp.png")
plt.figure()   #save pic in a lib
io.imshow(pic)
height,width,depth = pic.shape
print(height) #print first element of pic.shape that saved in int height
print(pic.shape) #print pixel size directly