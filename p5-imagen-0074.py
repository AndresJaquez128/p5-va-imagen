import cv2
# leer la imagen con cv2 = computer vision
img = cv2.imread("dalmata.jpg""")
# Determinar el tipo de imagen numpy.ndarray
print(type(img))
# Mostrar pixeles (980, 980, 3)
print(img.shape)
# Mostrando imagen en ventana barra de titulo 
cv2.imshow('dalmata 0074', img)
## Tiempo de espera
cv2.waitKey(0)
# Destruir toda la ventana
cv2.destroyAllWindows()