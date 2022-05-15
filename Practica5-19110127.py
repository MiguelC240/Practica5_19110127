import numpy as np 
import cv2 
from matplotlib import pyplot as plt

Img = cv2.imread('Img.jpg',0)
Res1 = cv2.resize(Img, dsize=(300, 300))
cv2.imshow('Imagen',Res1)


####################### Umbralización simple #################################



#ret,thresh = cv2.threshold(img, umbral, valorMax , tipo)


#img;       es la imagen gris que va a ser analizada
#umbral;    es el valor indicado a analizar en cada píxel
#valorMax;  Valor que se coloca a un píxel si sobrepasa el umbral
#tipo;      se elige un tipo de umbralización: THRESH_BINARY, THRESH_BINARY_INV,
#           THRESH_TRUNC, THRESH_TOZERO], THRESH_TOZERO_INV, THRESH_OTSU.


#La función devuelve:

#thresh;    imagen binarizada
#ret;       valor del umbral



################ THRESH_BINARY ################

# Los píxeles que superaron el umbral se les asigna el valor
# máximo establecido

ret,Treshbin = cv2.threshold(Res1,100,255,cv2.THRESH_BINARY)
cv2.imshow('Treshbin',Treshbin)



################ THRESH_BINARY_INV ################

# Los píxeles que superaron el umbral se les asigna 0 y a los
# que no superaron el umbral se les asigna el valor máximo establecido

ret,threshbin_inv = cv2.threshold(Res1,100,255,cv2.THRESH_BINARY_INV)
cv2.imshow('threshbin_inv',threshbin_inv)




################ THRESH_TRUNC ################

# Los píxeles que superaron el umbral se les asigna el mismo valor del
# umbral y a los que no superaron el umbral se les asigna los mismos valores
# que tenían originalmente

ret,threshtrunc = cv2.threshold(Res1,100,255,cv2.THRESH_TRUNC)
cv2.imshow('threshtrunc',threshtrunc)




################ THRESH_TOZERO ################

# Los píxeles que superaron el umbral mantienen el valor de los pixeles
# originalmente, y cuando no superan el umbral se les asigna cero

ret,threshtozero = cv2.threshold(Res1,100,255,cv2.THRESH_TOZERO)
cv2.imshow('threshtozero',threshtozero)


cv2.waitKey(0)
cv2.destroyAllWindows()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


cv2.imshow('Imagen',Res1)


################ THRESH_TOZERO_INV ################

# Los píxeles que superaron el umbral se les asigna cero, y a los píxeles
# que no superaron el umbral se les asigna el mismo valor que originalmente tenía


ret,threshtozero_inv = cv2.threshold(Res1,100,255,cv2.THRESH_TOZERO_INV)
cv2.imshow('threshtozero_inv',threshtozero_inv)





####################### Umbralización adaptativa #################################


# threshold = cv2.adaptiveThreshold(img,maxValue,adaptiveMethod,thresholdType,blockSize,C)



# img;              es una imagen de un solo canal, debe ser en escala de grises
# maxValue;         valor asignado a los pixeles cuando cumplen la condición
# adaptiveMethod;   método adaptativo, se elige entre cv.ADAPTIVE_THRESH_MEAN_C, cv.ADAPTIVE_THRESH_GAUSSIAN_C
# thresholdType;    elegir un método de umbralización
# blockSize;        Tamaño de una vecindad de píxeles que se utiliza para calcular un valor de umbral para el píxel: 3, 5, 7, etc
# C;                Constante restada de la media o media ponderada





################ THRESH_MEAN ################

thMean = cv2.adaptiveThreshold(Res1,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,7,7)
cv2.imshow('thMean',thMean)


################ THRESH_GAUSSIAN ################

thGaus = cv2.adaptiveThreshold(Res1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,20)
cv2.imshow('thGaus',thGaus)




################ THRESH_OTSU ################

ret1, thOtsu = cv2.threshold(Res1,100,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('thOtsu',thOtsu)


cv2.waitKey(0)
cv2.destroyAllWindows()
