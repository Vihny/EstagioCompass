## Comandos utilizados na etapa 1 do desafio

- ```docker build -t mascarar-dados .``` :  é usado para criar uma nova imagem Docker a partir de um Dockerfile. -t é a opção permite que nomeie e opcionalmente marque a imagem Docker, nesse caso mascarar-dados é o nome. O ponto no final do comando indica ao Docker para procurar o Dockerfile no diretório atual.

- ```docker images``` : é utilizado para listar todas as imagens Docker disponíveis no sintema.

- ```docker run -it mascarar-dados``` : é usado para executar um contêiner Docker em modo interativo com um terminal conectado, usando a imagem com o nome mascarar-dados.