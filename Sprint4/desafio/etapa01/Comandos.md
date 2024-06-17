## Comandos utilizados na etapa 1 do desafio

- ```docker build -t etapa1 .``` :  é usado para criar uma nova imagem Docker a partir de um Dockerfile. -t é a opção permite que nomeie e opcionalmente marque a imagem Docker, nesse caso etapa1 é o nome. O ponto no final do comando indica ao Docker para procurar o Dockerfile no diretório atual.

- ```docker images``` : é utilizado para listar todas as imagens Docker disponíveis no sintema.

- ```docker run 444f3124612c``` : Este comando irá criar e iniciar um novo contêiner Docker usando a imagem com o ID 444f3124612c.