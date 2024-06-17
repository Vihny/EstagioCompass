# Desafio

## Resposta Da Etapa 2
- É possível reutilizar containers? Em caso positivo, apresente o comando necessário para reiniciar um dos containers parados em seu ambiente Docker? Não sendo possível reutilizar, justifique sua resposta.
 R= Sim, é possível reutilizar containers no Docker pois quando um container é parado, ele não é destruído e pode ser reiniciado a qualquer momento. Para reiniciar um container é necessario ter o seu ID ou nome, pode obter essa informação utilizando o comando ```docker ps -a```. Depois pode reiniciar o container usando o comando ```docker start <nome_ou_id>```, esse comando retorna o ID ou nome conteiner isso significa que foi iniciado com sucesso.

 ## Comandos utilizados na etapa 2 do desafio

- ```docker ps -a``` :   é utilizado para listar todos os contêineres Docker do sistema, incluindo aqueles que estão parados (não em execução).

- ```docker start 970520c5e1a8``` :  é usado para iniciar um contêiner Docker que está parado. Quando este comando é executado, o Docker procura um contêiner com esse ID e, se encontrado e estiver parado, ele iniciará o contêiner.