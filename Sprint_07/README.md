## SPRINT 07

* ### *Learn By Example: Hadoop, MapReduce for Big Data problems:*
Hadoop é uma tecnologia essencial para o big data, pois trata do processamento de grandes volumes de dados de forma eficiente. O Hadoop é uma estrutura de código aberto que permite processar dados de forma distribuída. Sua principal característica é o HDFS (Hadoop Distributed File System), que divide e replica os dados em vários nós do cluster, garantindo alta disponibilidade e tolerância a falhas. Isso significa que mesmo se um nó falhar, os dados ainda estarão acessíveis a partir de outras cópias.

Uma das principais funcionalidades do Hadoop é o MapReduce, um modelo de programação que permite processar dados em paralelo no cluster. Ele é composto por duas fases: o mapper (mapeador) e o reducer (reduzidor). O mapper lê os dados de entrada e os transforma em pares chave-valor intermediários. Em seguida, o reducer combina esses pares chave-valor com base na chave e executa uma função específica para reduzi-los a um conjunto menor de pares chave-valor de saída.

O Hadoop também utiliza o YARN (Yet Another Resource Negotiator), um gerenciador de recursos que coordena e aloca recursos do cluster entre os aplicativos que estão sendo executados. O que garante que cada tarefa seja executada no nó adequado com a capacidade de processamento necessária.
___

* ### *Formação Spark com Pyspark : o Curso Completo:*

Apache Spark é um framework open-source para processamento de dados em escala, desenvolvido para lidar com tarefas de Big Data de forma eficiente e distribuída. Ele oferece velocidade, facilidade de uso e suporte para diversas linguagens de programação. Também suporta uma variedade de formatos de Big Data, como Hadoop Distributed File System (HDFS), Apache HBase, Apache Cassandra, Amazon S3, entre outros, o que possibilita a leitura e gravação de dados de várias fontes.

Sua arquitetura é baseada em um modelo de processamento em memória, permitindo que os dados sejam mantidos em RAM, o que acelera as operações. Seus principais componentes são o Spark Core, responsável pelas funcionalidades básicas, e os módulos Spark SQL, Spark Streaming, Spark MLlib e GraphX, que fornecem funcionalidades adicionais para processamento de SQL, streaming, aprendizado de máquina e processamento de grafos, respectivamente.

O spark manipula diversoso tipos de dados, dentre eles o RDD (Resilient Distributed Datasets) permitindo a representação de conjuntos de dados distribuídos e tolerantes a falhas. Ele suporta operações de transformação e ação para processar os dados. Também Datasets e DataFrames que são APIs de alto nível que permitem manipular dados estruturados de forma mais amigável do que RDDs, além de fornecer otimizações significativas de desempenho. Os DataFrames são fortemente tipados, enquanto os Datasets permitem que os dados sejam tratados como objetos fortemente tipados.

Além disso o Spark conta com o SparkContext que é a interface principal para interagir com um cluster Spark e que pode ser acessado através da criação de uma SparkSession, que oferece funcionalidades adicionais, como suporte a DataFrames e acesso ao Spark SQL.

O Spark também oferece uma ampla gama de ações e transformações que permitem realizar operações em RDDs, Datasets e DataFrames. As principais ações incluem `count()`, `collect()`, `saveAsTextFile()`, enquanto as transformações incluem `map()`, `filter()`, `groupBy()`, entre outras. Permite executar consultas SQL em RDDs, Datasets e DataFrames, facilitando a integração com sistemas legados. Além disso, é possível criar Views temporárias ou permanentes que representam consultas SQL pré-definidas. O Spark também suporta várias operações de join para combinar dados de diferentes fontes.

O Spark conta com o particionamento que é uma técnica utilizada para dividir conjuntos de dados em pedaços menores, permitindo a paralelização eficiente das operações. Bem como, o bucketing que é uma forma de particionamento específica para tabelas Hive, que agrupa dados em "buckets" com base em um ou mais campos, facilitando consultas mais rápidas.

Por fim, o Spark permite a persistência de dados em memória ou em disco, através de mecanismos como `cache()`, que armazena os resultados de um RDD, Dataset ou DataFrame em memória, e `persist()`, que permite definir níveis de armazenamento em cache, como MEMORY_ONLY, MEMORY_AND_DISK, etc., para equilibrar desempenho e consumo de recursos.
___

## ATIVIDADES

* [Exercicios Python 01](exercicios-python/exercicio_01.py)
* [Exercicios Python 01](exercicios-python/exercicio_02.py)
* [Exercicios Python 01](exercicios-python/exercicio_03.py)
* [Exercicios Python 01](exercicios-python/exercicio_04.py)
* [Exercicios Spark](exercicios-spark/README.md)
* [Lab Aws Glue](Lab_aws_glue/README.md)
* [Desafio Parte 1](/Desafio/parte_01/app/)
___


## CERTIFICADOS

* [Learn By Example: Hadoop, MapReduce for Big Data problems](certificados/certificado-hadoop.jpg)
* [Formação Spark com Pyspark : o Curso Completo](certificados/certificadp-curso-pyspark.jpg)

