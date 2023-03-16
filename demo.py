import numpy as np
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
    # Também é definida a velocidade e o estado iniciais.
    width = 320
    height = 180
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
        frame = cv.resize(frame, (width,height), interpolation=cv.INTER_AREA)

        # Inverte a imagem horizontalmente
        frame = cv.flip(frame, 1)

        # A variável image é um np.array com shape=(width, height, colors)
        image = np.array(frame).astype(float)/255
        image_ = np.zeros_like(image)

        Xd = criar_indices(0, height, 0, width)
        Xd = np.vstack ( (Xd, np.ones( Xd.shape[1]) ) )

        # Troca a rotacao da imagem de acordo com o estado atual
        if cmd == 'rotate-counterclockwise':
            speed += 0.1
        if cmd == 'rotate-clockwise': 
            speed -= 0.1

        # Configura as matrizes de transposicao e rotacao
        T = np.array([[1, 0, -height/2], [0, 1, -width/2], [0, 0,1]])
        R = np.array([[np.cos(speed), -np.sin(speed), 0], [np.sin(speed), np.cos(speed), 0], [0, 0,1]]) # Matriz de rotação.
        T2 = np.array([[1, 0, height/2], [0, 1, width/2], [0, 0,1]])

        # Junta as matrizes acima em uma só para aplicar a transformação
        A = T2 @ R @ T

        # Aplica a transformação
        X = np.linalg.inv(A) @ Xd
        X = X.astype(int)
        Xd = Xd.astype(int)

        # Tira os pixels fora da tela para evitar crashes
        Xd[0,:] = np.clip(Xd[0,:], 0, image_.shape[0])
        Xd[1,:] = np.clip(Xd[1,:], 0, image_.shape[1])

        filtro = ((X[0,:]>= 0 ) & (X[0,:] < image_.shape[0]) & (X[1,:] < image_.shape[1]))
        Xd = Xd[:,filtro]
        X = X [:,filtro]

        image_[Xd[0,:], Xd[1,:], :] = image[X[0,:], X[1,:], :]

        # Agora, mostrar a imagem na tela!
        cv.imshow('Minha Imagem!', image_)
        
        # INPUTS
        if cv.waitKey(1) == ord('q'): # Sai do loop e fecha o programa
            break
        if cv.waitKey(1) == ord('a'): # Gira sentido anti-horario
            cmd = 'rotate-counterclockwise'
        if cv.waitKey(1) == ord('s'): # Para de girar
            cmd = 'idle'
        if cv.waitKey(1) == ord('d'): # Gira sentido horario
            cmd = 'rotate-clockwise'


    # Ao sair do loop, vamos devolver cuidadosamente os recursos ao sistema!
    cap.release()
    cv.destroyAllWindows()

run()
