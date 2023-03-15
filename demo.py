import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2 as cv
import pandas as pd

# Matriz RGB -> YIQ
A = np.array( [[0.299, 0.587, 0.144], [0.5959, -0.2746, -0.3213], [0.2115, -0.5227, 0.3112]] )

def distorcao_de_cor():
    # --- boilerplate code
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Não consegui abrir a câmera!")
        exit()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Não consegui capturar frame!")
            break
    # --- fim do boilerplate code

        # A variável image é um np.array com shape=(height, width, colors)
        

        image = np.array(frame).astype(float)/255
        H, W, C = image.shape
        #print(image.shape)
        X = image.reshape(H*W, C).T
        # --- vamos trabalhar nesta parte


        # --- fim da parte que vamos trabalhar
        image = X.T.reshape(H, W, C)

    # --- mais boilerplate code
        # Agora, mostrar a imagem na tela!
        cv.imshow('Distorcao_de_cor', image)
        
        # Se aperto 'q', encerro o loop
        # Use esse tipo de estrutura para implementar as outras interações!
        if cv.waitKey(1) == ord('q'):
            break

        if cv.waitKey(1) == ord('w'):
            print('lmao')

    cap.release()
    cv.destroyAllWindows()
    # --- fim do boilerplate code - e da função!

distorcao_de_cor()