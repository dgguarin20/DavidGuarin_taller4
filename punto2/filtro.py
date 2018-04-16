import numpy as np
from PIL import Image
from scipy.fftpack import convolve2d

imagen = raw_input("nombre imagen")
n = raw_input("n")
im = Image.open("imagen.jpg")

imarray = np.array(im)
imarray2 = imarray
row = len(imarray)
col = len(imarray[0])



t = np.linspace(-10,10,20)
bump = np.exp(-0.05*t**2)
bump = bump/np.trapz(bump)

kernel = bump[:,np.newaxis]*bum[np.newaxis,:]

kernel_ft = fftpacl.fft2(kernel, shape=img.shape[:2], axes(0,1))
for i in range(0,len(kernel_ft)):
    for j in range(0, len(kernel_ft[0])):
        for k in range(0,3):
            a = kernel_ft[i,j]
            if (a[k]<n):
                kernel_ft[i,j]=0

img_ft = fftpack.fft2(im, axes(0,1))
img2_ft = kernel_ft[:,:,np.newaxis]*img_ft
img2 = fftpack.ifft2(img2_ft,axes=(0,1)).real

img = Image.fromarray(imarray2, 'RGB')
img.save('result.png')
img.show()
