1. Construa uma imagem a partir de um arquivo de instruções (Dockerfile) que execute o código carguru.py. Após, execute um container a partir da imagem criada.
Registre aqui o conteúdo de seu arquivo Dockerfile e o comando utilizado para execução do container. -->


2. É possível reutilizar containers? Em caso positivo, apresente o comando necessário para reiniciar um dos containers parados em seu ambiente Docker? Não sendo possível reutilizar, justifique sua resposta.

RESPOSTA: Sim, é possível reutilizar containers no Docker. Para reiniciar um container parado, você pode usar o comando docker start <nome-do-container>. No entanto, é necessário fazer algumas observações: se o container for criado com a opção --rm que remove automaticamente quando ele for interrompido, não será possível reutilizá-lo. Também se um container tiver sua imagem atualizada ou removida, será necessário criar um novo container com base na imagem atualizada.
