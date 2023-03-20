# efeito_de_rotacao_video-

Pedro Antônio SIlva e ________

https://github.com/P-ASilva/efeito_de_rotacao_video-.git

- TASKS :

Tirar artifacting (consultar notebook aula 3)

Limpar e comentar código

Escrever o README.md (checar rubrica)

Tentar fazer até o requisito A, depois a gente vê se ta com vontade de seguir adiante

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

A - Rotacionar a imagem no sentido anti-horário.

D - Rotacionar a imagem no sentido anti-horário.

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

\cos(speed), -\
\sin(speed), 0 \\

\sin(speed), \cos(speed), 0 \\

0, 0,1

\end{bmatrix}
T2 =
\begin{bmatrix}

1, 0, H/2 \\

0, 1, W/2 \\

0, 0,1

\end{bmatrix}

$$
Onde a matriz T, faz uma translação da matriz de imagem para o centro da tela.
$$
T =

\begin{bmatrix}

1, 0, -H/2 \\

0, 1, -W/2 \\

0, 0 , 1

\end{bmatrix}

$$

A matriz R faz com que a matriz imagem rotacione em torno de seu canto superior esquerdo. Esse é o motivo pelo qual devemos transpor a matriz inicialmente, sabendo que não há outra forma direta de rotacioná-la em torno de seu centro. 

$$
R =
\begin{bmatrix}

\cos(speed), -\
\sin(speed), 0 \\

\sin(speed), \cos(speed), 0 \\

0, 0,1

\end{bmatrix}
$$

E finalmente, a matriz T2 faz com que a imagem seja transladada de volta para sua posição inicial, "consertando" assim seu posicionamento para o centro da tela, dado que a rotação a desloca para baixo e para a direita.
$$
\begin{bmatrix}

1, 0, H/2 \\

0, 1, W/2 \\

0, 0,1

\end{bmatrix}
$$

Descritivo das variáveis :

- A variável speed, atualizada com o tempo, muda o ângulo de rotação da matriz, o que faz com que ela gire.
- As variaveis W e H representam a largura e altura respectivamente.


Juntamos essas matrizes na seguinte forma, para facilitar na hora do calculo :  

$$
A = T2 * R * T 
$$

E a aplicamos no seguinte calculo com X, que prepresenta um mapeamento dos pixeis da imagem.

$$
X = inv(A) * Xd
$$