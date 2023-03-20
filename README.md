# efeito_de_rotacao_video-

Pedro Antônio Silva e Gustavo Lindenberg Pacheco

https://github.com/P-ASilva/efeito_de_rotacao_video-.git

## Como instalar e executar

- Instale o Python (https://www.python.org/) em sua máquina. O programa foi desenvolvido especificamente para Windows, portanto não há garantia de que funcionará em outros sistemas operacionais.

- Instale algum editor de texto/código, como o Visual Studio Code (https://code.visualstudio.com/).

- Abra o Visual Studio Code, procure pela opção Clonar Repositório, e selecione Clonar da Internet. No campo, cole o seguinte link: https://github.com/P-ASilva/efeito_de_rotacao_video-.git

- Escolha uma localização em sua máquina para salvar o repositório clonado.

- Abra o terminal e digite o comando a seguir:

> pip install -r "requirements.txt"

- No Visual Studio, abra o arquivo "demo.py" dentro do repositório clonado. Você poderá usá-lo para testar o código.

## Como usar o programa

Para inicializar a camera, apenas rode o arquivo demo.py no sua IDE de preferência, uma vez com a cmera aberta, você pode usar os seguintes comandos no teclado:

A - Rotacionar a imagem pno sentido anti-horário.

D - Rotacionar a imagem no sentido anti_horário.

S - Parar a rotação.

Q - Encerrar programa.

## Modelo Matemático

Primeiro inicialisamos uma matriz de base Xd, que espelha as dimensões da imagem recebida pela camera H = 180 e W = 320 e depois disso configuramos as matrizes :

$$

T =

\begin{bmatrix}

1, 0, -H/2 \\

0, 1, -W/2 \\

0, 0 , 1

\end{bmatrix}
R =
\begin{bmatrix}

cos(speed), -np.sin(speed), 0 \\

np.sin(speed), np.cos(speed), 0 \\

0, 0,1

\end{bmatrix}
T2 =
\begin{bmatrix}

1, 0, height/2 \\

0, 1, width/2 \\

0, 0,1

\end{bmatrix}

$$

A matriz T, faz uma transposição da matriz de imagem para o centro da tela.

Já a matriz R faz com que a matriz imagem rotacione em torno de seu canto superior esquerdo. Esse é o motivo pelo qual devemos transpor a matriz inicialmente, sabendo que não há outra forma direta de rotacioná-la em torno de seu centro. 

A variável speed, atualizada com o tempo, muda o ângulo de rotação da matriz, o que faz com que ela gire.

Finalmente, a matriz T2 faz com que a imagem seja transposta de volta para sua posição inicial, "consertando" assim seu posicionamento para o centro da tela, dado que a rotação a desloca para baixo e para a direita.

Juntamos essas matrizes na forma de  A = T2 @ R @ T e pré-multiplicamos A^-1 por Xd e armazenamos como X, com Xd e X sendo usados para se representar a imagem dentro do código, 

Adicionalmente, colocamos um filtro para que a matriz não representase pontos fora do domínio da imagem e aplicamos o conceito de remoção de artefatos visto em aula, como elaborado abaixo :

### Retirando artefatos da imagem

Talvez, ao realizar uma rotação, você veja a sua imagem resultante cheia de pontinhos. Isso acontece porque nem todo ponto na imagem de destino tem um correspondente na imagem de origem. Então, podemos solucionar isso usando a seguinte ideia:

$$
X_d = A X_o
$$

Os pixels de $X_o$ estão bem organizados em uma grade, mas os pixels de $X_d$ não, e é isso que leva ao surgimento desses pontinhos pretos no meio da imagem. Porém, nada impede que façamos os pixels de $X_d$ como uma grade, e então encontremos os pixels em $X_o$ correspondentes usando a transformação inversa:

$$
X_o = A^{-1} X_d
$$

Referência : Notebook 3 de Algebra Linear, explicação e exemplo elaborados pelo Professor Tiago, 2023.