import numpy as np
import matplotlib.pyplot as plt
import skimage
import cv2
from skimage import io

def add_noise(img, mode, r, c, i):
    plt.subplot(r,c,i)
    if mode is not None:
        gimg = skimage.util.random_noise(img, mode=mode)
        plt.imshow(gimg)
    else:
        plt.imshow(img)
    plt.title(mode)
    plt.axis("off")

img=skimage.io.imread('watch.jpg')/255.0
plt.figure(figsize=(6,8))
r,c=4,2
add_noise(img,'gaussian',r,c,1)   #gaussian distributed random additive noise
add_noise(img,'localvar',r,c,2)   #gaussian distributed random additive noise with specified local vaiance at each piont
add_noise(img, "poisson", r,c,3)  #poisson distributed noise generated by image
add_noise(img, "salt", r,c,4)     #replace random pixels with 1
add_noise(img, "pepper", r,c,5)   #replace random pixels with 0
add_noise(img, "s&p", r,c,6)      #replace random pixels with 0 and 1
add_noise(img, "speckle", r,c,7)  #multiplicative noise (img=img+n*img) with sepcified mean and variance
add_noise(img, None, r,c,8)
plt.show()