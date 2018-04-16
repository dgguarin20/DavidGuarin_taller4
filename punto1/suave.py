import numpy as np
from PIL import Image


imagen = raw_input("nombre imagen")
n = raw_input("n")
im = Image.open("imagen.jpg")

imarray = np.array(im)
imarray2 = imarray
row = len(imarray)
col = len(imarray[0])

#esto es la matriz donde se divide por su suma para que de 1. y asi esto es que hagarra los de centro para 
#sacar la gausiana
gauss = [[0, 1, 2, 1, 0],[1, 3, 5, 3, 1],[ 2, 5, 9, 5, 2],[ 1, 3, 5, 3, 1],[0, 1, 2, 1, 0]]
gauss = np.asarray(gauss)
gauss = (1.0/57)*gauss

retornoimagen = np.zeros((row,col))


for i in range(2, row-2 ):

    for j in range(2, col-2):
        suma = 0
        for k in range(-2,3):

            for l in range(-2,3):
                #para sacar las del centro del gauss.
                suma = suma+ imarray[i+k,j+l]*gauss[2+k,2l]

       
        imarray2[i,j]=suma

img = Image.fromarray(imarray2, 'RGB')
img.save('result.png')
img.show()
