# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 14:54:15 2017

@author: tkustaff
"""

import os, numpy, PIL
from PIL import Image

# Access all PNG files in directory
allfiles=os.listdir(os.getcwd())
imlist=[filename for filename in allfiles if  filename[-4:] in [".jpg",".JPG"]]#

w,h=Image.open(imlist[0]).size
N=len(imlist)

arr=numpy.zeros((h,w),numpy.float)#

wei = {1/10,1/10,2.0/10,2.0/10,2.0/10,1/10,2.0/10,1/10,1/10,1/10}

for im in imlist:
    imarr=numpy.array(Image.open(im),dtype=numpy.float)
    arr=arr+(imarr*wei[im])
    
    #2346
arr=numpy.array(numpy.round(arr),dtype=numpy.uint8)

out=Image.fromarray(arr)#
out.save("Average.png")
out.show()