import numpy as np
#import keyboard

# Instalar a biblioteca cv2 pode ser um pouco demorado. Não deixe para ultima hora!
import cv2 as cv

def criar_indices(min_i, max_i, min_j, max_j):
    import itertools
    L = list(itertools.product(range(min_i, max_i), range(min_j, max_j)))
    idx_i = np.array([e[0] for e in L])
    idx_j = np.array([e[1] for e in L])
    idx = np.vstack( (idx_i, idx_j) )
    return idx

def run():
    # Essa função abre a câmera. Depois desta linha, a luz de câmera (se seu computador tiver) deve ligar.
    cap = cv.VideoCapture(0)

    # Aqui, defino a largura e a altura da imagem com a qual quero trabalhar.
    # Dica: imagens menores precisam de menos processamento!!!
    width = 640
    height = 360

    speed = 0

    cmd = 'idle'

    # Talvez o programa não consiga abrir a câmera. Verifique se há outros dispositivos acessando sua câmera!
    if not cap.isOpened():
        print("Não consegui abrir a câmera!")
        exit()

    # Esse loop é igual a um loop de jogo: ele encerra quando apertamos 'q' no teclado.
    while True:
        # Captura um frame da câmera
        ret, frame = cap.read()

        # A variável `ret` indica se conseguimos capturar um frame
        if not ret:
            print("Não consegui capturar frame!")
            break

        # Mudo o tamanho do meu frame para reduzir o processamento necessário
        # nas próximas etapas
        frame = cv.resize(frame, (width,height), interpolation =cv.INTER_AREA)
        frame = cv.flip(frame, 1)
        # A variável image é um np.array com shape=(width, height, colors)
        image = np.array(frame).astype(float)/255
        
        image_ = np.zeros_like(image)

        X = criar_indices(0, height, 0, width)
        X = np.vstack ( (X, np.ones( X.shape[1]) ) )

        if cmd == 'rotate-counterclockwise':
            speed += 0.1
        if cmd == 'rotate-clockwise': 
            speed -= 0.1

        R = np.array([[np.cos(speed), -np.sin(speed), 0], [np.sin(speed), np.cos(speed), 0], [0, 0,1]]) # Matriz de rotação.
        #R = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

        Xd = R @ X
        Xd = Xd.astype(int)
        X = X.astype(int)

        # Troque este código pelo seu código de filtragem de pixels
        Xd[0,:] = np.clip(Xd[0,:], 0, image_.shape[0])
        Xd[1,:] = np.clip(Xd[1,:], 0, image_.shape[1])

        filtro = ((Xd[0,:]>= 0 ) & (Xd[0,:] < image_.shape[0]) & (Xd[1,:] < image_.shape[1]))
        Xd = Xd[:,filtro]
        X = X [:,filtro]

        image_[Xd[0,:], Xd[1,:], :] = image[X[0,:], X[1,:], :]

        # Agora, mostrar a imagem na tela!
        cv.imshow('Minha Imagem!', image_)
        
        # Se aperto 'q', encerro o loop
        if cv.waitKey(1) == ord('q'):
            break

        if cv.waitKey(1) == ord('a'):
            cmd = 'rotate-counterclockwise'
        if cv.waitKey(1) == ord('s'):
            cmd = 'idle'
        if cv.waitKey(1) == ord('d'):
            cmd = 'rotate-clockwise'


    # Ao sair do loop, vamos devolver cuidadosamente os recursos ao sistema!
    cap.release()
    cv.destroyAllWindows()

run()
