## SPRINT 06


* ### *Data Analytics Fundamentals:*

O curso apresenta os 5 Vs do Big Data - Volume, Velocidade, Variedade, Veracidade e Valor e descreve os principais problemas relacionados à análise de dados e quais as possíveis soluções oferecidas pela AWS.
Os 5 Vs são elementos essenciais que descrevem os desafios e características do gerenciamento e análise de grandes volumes de dados. 

* VOLUME: Diz respeito à quantidade massiva de dados que são gerados diariamente. O principal problema relacionado ao volume de dados é a capacidade de armazenamento e processamento. Lidar com grandes quantidades de dados pode sobrecarregar a infraestrutura de hardware e tornar a análise de dados mais lenta. O Amazon S3 é um serviço de armazenamento em nuvem escalável e altamente durável da AWS. Ele permite armazenar e recuperar grandes volumes de dados de forma eficiente. Além disso, o Amazon Redshift é um serviço de data warehousing que oferece um ambiente escalável para análise de dados em grande escala.

* VELOCIDADE: Refere-se à necessidade de processar e analisar dados em tempo real ou próximo disso. O desafio é lidar com a ingestão rápida de dados e garantir que a análise ocorra em tempo hábil para tomar decisões em tempo real. A AWS oferece o Amazon Kinesis que é um serviço que permite a ingestão, processamento e análise de streaming de dados em tempo real. Ele pode lidar com grandes volumes de dados em tempo real, fornecendo insights instantâneos para tomada de decisões rápidas.

* VARIEDADE: A variedade é sobre a diversidade dos tipos e formatos de dados disponíveis, como dados estruturados, semiestruturados e não estruturados. O desafio é combinar e analisar efetivamente esses diferentes tipos de dados para obter insights significativos. O Amazon Glue é um serviço de preparação e transformação de dados que pode ser usado para descobrir, catalogar e transformar dados de diferentes fontes em um formato adequado para análise. Ele automatiza tarefas de preparação de dados, ajudando a lidar com a variedade de dados.

* VERACIDADE A veracidade refere-se à confiabilidade e qualidade dos dados. Os dados podem conter erros, duplicatas ou estar incompletos, o que pode afetar a precisão das análises e tomadas de decisão. O AWS Data Pipeline é um serviço que ajuda a orquestrar e agendar fluxos de trabalho de processamento de dados. Ele permite limpar, transformar e validar os dados antes de enviá-los para análise, ajudando a garantir a veracidade dos dados.

* VALOR: Por último, o valor refere-se à capacidade de extrair insights significativos e relevantes dos dados para obter benefícios comerciais. O desafio é identificar e usar corretamente os dados que são mais valiosos para a organização. Para isso a AWS oferece diversos serviços de análise de dados, como o Amazon Athena, que permite consultar dados diretamente no Amazon S3 usando SQL padrão; o Amazon EMR (Elastic MapReduce), que fornece uma plataforma de processamento de big data escalável; e o Amazon QuickSight, um serviço de visualização de dados que ajuda a criar painéis interativos e compartilháveis.
___


* ### *Data Analytics on AWS (Business):*

O curso começa com uma descrição das oportunidades de mercado e fornece exemplos do setor objetivando capacitar parceiros a identificar e qualificar oportunidades de negócios em análise de dados. São apresentadas técnicas recomendadas para conduzir conversas de forma eficaz para descobrir negócios e alinhas as melhores soluções em análise de dados, dessa forma criando um plano de ação e exploção de recursos disponíveis para o cliente.

O curso ainda discorre sobre as etapas consideradas importante ao projetar uma arquitetura de dados eficiente e escalável. Como modernizar um data warehouse usando o Amazon Redshift, quais suas vantagens e como funcionao processo. Como criar um data lake que é um repositório centralizado de dados brutos. São abordados os serviços da AWS que permitem a criação de um data lake escalável e seguro, bem como as melhores práticas para sua implementação. São apresentadas soluções para transmissão de dados em tempo real e análise preditiva. Como capturar, processar e analisar dados em tempo real, bem como utilizar algoritmos de aprendizado de máquina para gerar insights preditivos a partir dos dados.

Também é abordada a importância da governança de dados na análise de dados. Quais recursos e práticas recomendadas da AWS para garantir a qualidade, segurança e conformidade dos dados durante todo o ciclo de vida. Além disso também sao tratados assuntos como: qual o público-alvo desse tipo de venda, como conduzir uma conversa e melhor responder aos questionamentos e objeções dos clientes.
___


* ### *Introduction to Amazon Kinesis Streams:*

No curso foi apresentado o serviço Amazon Kinesis Stream que é um serviço de streaming de dados da AWS projetado para coletar, processar e analisar grandes volumes de dados em tempo real. 

O Kinesis Stream é um serviço de streaming de dados fornecido pela Amazon Web Services (AWS) Ele é projetado para coletar, processar e analisar grandes volumes de dados em tempo real. Os dados podem ser enviados para um stream de várias maneiras, como usando a API do Kinesis, bibliotecas do Kinesi Producer, integração com outras ferramentas da AWS ou por meio de serviços de terceiros. Também permite a utilização de recursos de dimensionamento automático, garantindo o processamento e ingestaçõ de dados de forma consistente e eficiente.
___


* ### *Introduction to Amazon Kinesis Analytics:*

O Amazon Kinesis Analytics é um serviço da AWS para analisar e processar dados em tempo real usando consultas SQL. Por ser integrado com o Amazon Kinesis Streams e o Amazon Kinesis Firehose, permite realizar consultas em tempo real nos dados do stream e extrair informações deles. Atavés da interface visual chamada Kinesis Analytics Studio é possível fazer consultas SQL e visualizar os resultados em tempo resal. 
É altamente escalável e dimensiona de forma dinâmica a capacidade de processsamento de acordo com a quantidade dados sendo utilizados. Possui integração com outros serviços da AWS tais como S3, Redshift, Elasticsearch possibilitando o envio das consultas para outros destinos.
___


* ### *Introduction to Amazon Elastic MapReduce(EMR):*

Conforme demonstrado no curso, o EMR é um serviço da AWS que simplifica o processamento de grandes volumes de dados em ambiente distribuído. O EMR fornece uma estrutura gerenciada e escalável para executar tarefas, provisionar recursos, gerenciar cluster, tolerância a falhas e monitoramente, deixando o usuário livre para realizar a lógica de negócios no processamento de dados. Por ser altamente escalável, permite a execução de tarefas em paralelo em um cluster de máquinas virtuais, dimensionando automaticamente a capacidade de acordo com a carga de trabalho. Por ser integrado a outros serviços da AWS como o S3 o Amazon DynamoDB permite o acesso e processamento dos dados armazenados nesses serviços. 

O serviço é altamente escalável e pode lidar com grandes volumes de dados. Ele permite que você execute tarefas de processamento de dados em paralelo em um cluster de máquinas virtuais, dimensionando automaticamente a capacidade de acordo com a carga de trabalho. Isso garante que você possa processar grandes conjuntos de dados de forma rápida e eficiente.
___


* ### *Introduction to Amazon Athena:*

O Amazon Athena é um serviço de consulta interativo que permite analisar dados armazenados no Amazon S3 usando consultas SQL. Com o Athena, é possível executar consultas *ad-hoc* em grandes volumes de dados sem a necessidade de configurar ou gerenciar infraestrutura.
 
O serviço suporta consultas SQL é compatível com vários formatos de dados, como CSV, JSON, Parquet e outros. Ele também oferece recursos avançados, como particionamento de dados, que permite a organização dos dados em diretórios no S3 para melhorar o desempenho das consultas, e consultas federadas, que permitema execução de consultas que combinam dados do S3 com outros serviços da AWS, como o Amazon DynamoDB. É um serviço altamente escalável permitindo lidar com grandes volumes de dados, além disso permite integração com outras ferramentas e serviços da AWS. 
___


* ### *Introduction to Amazon Quicksight:*

Serve para realizar a visualização de dados. Permite criar, visualizar e compartilhar panéis interativos e relatórios de dados de forma rápida e fácil. Possibilita conectar com várias fontes de dados, como banco de dados, planilhas e arquivos CSV para criar visualizações. Possui recursos de análise, cálculos, filtragem de dados, inteligência artificial, análise preditiva e detecção automática de anomalias. É altamente escalável e permite a integração com outros serviços da AWS
___


* ### *Introduction to AWS IoT Analytics:*

O AWS IoT Analytics é um serviço gerenciado que facilita a análise de grandes volumes de dados da IoT. Ele automatiza etapas complexas, como filtragem, transformação e enriquecimento dos dados, antes de armazená-los em um repositório de séries temporais. O serviço suporta consultas ad hoc usando SQL embutido e análises mais avançadas, incluindo aprendizado de máquina. Além disso, permite a execução de análises personalizadas em contêineres. Com escalabilidade automática e pagamento conforme o uso, o AWS IoT Analytics oferece uma solução simples e eficiente para obter insights valiosos a partir de dados da IoT, sem a necessidade de gerenciar infraestrutura.

Em resumo, o AWS IoT Analytics simplifica a análise de dados da IoT, automatizando tarefas complexas e fornecendo recursos como filtragem, transformação e enriquecimento de dados. Com suporte a consultas SQL, análises avançadas e aprendizado de máquina, o serviço ajuda a obter insights precisos a partir dos dados da IoT. Além disso, o AWS IoT Analytics oferece escalabilidade automática e um modelo de pagamento flexível, eliminando a necessidade de gerenciar a infraestrutura subjacente. Com isso, as empresas podem tomar decisões mais informadas e aproveitar ao máximo seus dados da IoT.

___


* ### *Getting Started with Amazon RedShift:*

O Amazon Redshift é um serviço de data warehousing projetado para processar, armazenar e analisar grandes volumes de dados estruturados de forma eficiente e escalável. Utiliza uma arquitetura de banco de dados colunar, o que reduz o consumo de recursos. Ele é otimizado para consultas analíticas e suporta consultas SQL complexas em grandes conjuntos de dados.

É altamente escalável, permitindo aumentar ou diminuir a capacidade de armazenamento e o poder de processamento conforme necessário, sem interromper a operação. Isso permite que as empresas dimensionem seus clusters do Redshift de acordo com a demanda, garantindo desempenho consistente e eficiente.

O Redshift é integrado com outras ferramentas e serviços da AWS, como o Amazon S3, o AWS Glue e o AWS Data Pipeline. Isso permite carregar facilmente dados no Redshift a partir dessas fontes, automatizar processos de ETL e criar pipelines de dados completos para análise. 
___


* ### *Deep Dive into Concepts and Tools for Analyzing Streaming Data:*

O curso apresenta conceitos e ferramentas sobre análise de dados de streaming. O processamento de dados de streaming envolve a análise contínua de dados em tempo real, apresentando desafios devido ao volume e velocidade dos dados. Estratégias como segmentação temporal e escolha da semântica de tempo adequada são comumente usadas para lidar com esses desafios. Além disso, o gerenciamento do estado é essencial, permitindo armazenar e atualizar informações relevantes ao longo do fluxo de dados. A AWS oferece serviços como Amazon Kinesis Data Streams, Amazon Kinesis Data Analytics e AWS Lambda para processamento de dados de streaming, permitindo consultas em tempo real e análise eficiente. Esses serviços ajudam as empresas a implementar soluções robustas de processamento de dados de streaming e obter insights valiosos em tempo real.
___


* ### *Best Practices for Data WareHousing with Amazon RedShift:*

O curso fala sobre as melhores práticas para criação e manutenção de um data warehouse utilizando o Amazon Redshift, quais sejam:

* Modelagem dimensional: Envolve a criação de esquemas de estrela ou floco de neve, com tabelas de fatos e dimensões, para otimizar consultas analíticas.

* Distribuição de dados: Recomenda-se distribuir os dados com base em chaves de junção comuns para minimizar o movimento de dados durante as consultas.

* Ordenação de dados: É recomendado ordenar as tabelas com base em colunas que são frequentemente usadas em operações de junção.

* Compressão de dados: Recomenda-se usar a compressão por coluna, escolhendo o tipo de compressão adequado para cada tipo de dados.

* Carregamento e atualização de dados: Para atualizações incrementais, é recomendado o uso de operações de inserção em massa ou mesclagem.

* Monitoramento e ajuste de desempenho: Recomenda-se usar as ferramentas de monitoramento e os recursos de visualização de consultas disponíveis para identificar gargalos de desempenho e otimizar consultas.

* Backup e segurança: É fundamental implementar práticas de backup e recuperação de dados para proteger suas informações. O Amazon Redshift oferece opções de backup automatizado, e é recomendado criar snapshots regularmente.

* Escalabilidade: O Amazon Redshift permite dimensionar verticalmente  e horizontalmente. Monitorar a carga de trabalho e ajustar a escala do cluster conforme necessário é uma prática recomendada.
___


* ### *Serverless Analytics:*

O curso fala sobre Serverless analytics que é uma abordagem que aproveita o poder das ferramentas e serviços em nuvem, como AWS IoT Analytics, Amazon Cognito, AWS Lambda e Amazon SageMaker, para sintetizar e processar dados provenientes de diferentes fontes de maneira eficiente e escalável.

eAo combinar essas ferramentas e serviços, é possível agregar, processar, armazenar e disponibilizar dados úteis de maneiras inovadoras e poderosas. Os dados podem ser capturados e filtrados pelo AWS IoT Analytics, autenticados e autorizados pelo Amazon Cognito, processados e acionados pelas funções do AWS Lambda e, em seguida, utilizados para treinar e implantar modelos com o Amazon SageMaker.

Essa abordagem serverless permite uma arquitetura flexível, escalável e altamente automatizada, eliminando a necessidade de gerenciar infraestrutura e recursos manualmente. Além disso, ela possibilita o processamento em tempo real e a entrega de insights rápidos e relevantes para apoiar a tomada de decisões informadas e impulsionadas por dados.

___


* ### *Why Analytics for Games:*

O curso demosntra que a análise de dados em jogos traz diversos benefícios, como aprimorar o design do jogo, aumentar a eficiência das operações e embasar decisões financeiras e estratégicas. Por meio da análise, é possível tomar decisões rápidas e bem informadas para melhorar a jogabilidade, promover o engajamento dos jogadores e aumentar a receita. Para isso a AWS oferece uma variedade de serviços de análise para atender às necessidades de desenvolvimento de jogos, dessa forma é importante identificar os dados a serem mensurados e capturá-los dos sistemas de origem, como clientes de jogos, servidores de jogos e serviços de back-end.

Ao compreender os tipos de dados disponíveis, como conteúdo de texto, mídia social, áudio, vídeo, entre outros, é possível obter insights valiosos. No entanto, é necessário considerar as restrições e desafios que surgem devido à variedade de opções de dados. Um pipeline de análise é essencial para transformar os dados do jogo em respostas úteis. Esse pipeline deve ser projetado de forma flexível, permitindo entregar insights tanto em tempo real quanto em lotes, para atender às demandas dos consumidores de dados.

Em resumo, a análise de dados em jogos com a ajuda dos serviços da AWS permite entender os jogadores, desenvolver jogos de forma eficaz e criar elementos de jogabilidade que despertem o interesse e levem à compra por parte dos jogadores.



___
## CERTIFICADOS

Em razão da AWS não fornecer certificado para as vídeo-aulas, foram tirados prints demonstrando a conclusão dos respectivos cursos.

* [Data Analytics Fundamentals](certificados/certificado-data-analytics-fundamentals.png)
* [Data Analytics on AWS (Business)](certificados/certificado-data-analytics-on-aws.png)
* [Introduction to Amazon Kinesis Streams](certificados/certificado-introduction-amazon-kinesis-stream.png)
* [Introduction to Amazon Kinesis Analytics](certificados/certificado-introduction-amazon-kinesis-analytics.png)
* [Introduction to Amazon Elastic MapReduce(EMR)](certificados/certificado-introduction-amazon-emr.png)
* [Introduction to Amazon Athena](certificados/certificado-introduction-amazon-athena.png)
* [Introduction to Amazon Quicksight](certificados/certificado-introduction-amazon-quicksight.png)
* [Introduction to AWS IoT Analytics](certificados/certificado-amazon-iot-analytics.png)
* [Getting Started with Amazon RedShift](certificados/certificado-amazon-redshift.png)
* [Deep Dive into Concepts and Tools for Analyzing Streaming Data](certificados/certificado-concepts-tools-analyzing-streaming-data.png)
* [Best Practices for Data WareHousing with Amazon RedShift](certificados/certificado-practices-data-warehousing-redshift.png)
* [Serverless Analytics](certificados/certificado-serverless-analytics.png)
* [Why Analytics for Games](certificados/certificado-analytics-for-games.png)
___

## Laboratórios

* [Lab AWS S3](Lab_aws_s3/README.md)
* [Lab AWS Athena](Lab_aws_athena/README.md)
* [Lab AWS Lambda](Lab_aws_lambda/README.md)
* [Lab AWS Limpeza de Recursos](Lab_aws_limpeza_recursos/README.md)

