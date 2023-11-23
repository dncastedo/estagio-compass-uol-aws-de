import boto3
import csv
import json
from io import StringIO
import requests
from datetime import datetime

def processar_registros(registros, chave_api, s3, bucket, data_atual):
    ids_processados = set()
    for row in registros:
        id_filme = row['id']
        ano_lancamento = row['anoLancamento']
        genero = row['genero']

        if id_filme not in ids_processados:
            ids_processados.add(id_filme)

            
            if (ano_lancamento == '\\N' or (1894 <= int(ano_lancamento) <= 1909)) and (genero == 'Horror' or genero == 'Mistery'):
            # if (ano_lancamento == '\\N' or (1910 <= int(ano_lancamento) <= 1920)) and (genero == 'Horror' or genero == 'Mistery'):
            # if (ano_lancamento == '\\N' or (1921 <= int(ano_lancamento) <= 1929)) and (genero == 'Horror' or genero == 'Mistery'):
            # if (ano_lancamento == '\\N' or (1930 <= int(ano_lancamento) <= 1939)) and (genero == 'Horror' or genero == 'Mistery'):
            # if (ano_lancamento == '\\N' or (1940 <= int(ano_lancamento) <= 1949)) and (genero == 'Horror' or genero == 'Mistery'):
            # if (ano_lancamento == '\\N' or (1950 <= int(ano_lancamento) <= 1959)) and (genero == 'Horror' or genero == 'Mistery'):
            # if (ano_lancamento == '\\N' or (1960 <= int(ano_lancamento) <= 1969)) and (genero == 'Horror' or genero == 'Mistery'):
            # if (ano_lancamento == '\\N' or (1970 <= int(ano_lancamento) <= 1979)) and (genero == 'Horror' or genero == 'Mistery'):
            # if (ano_lancamento == '\\N' or (1980 <= int(ano_lancamento) <= 1989)) and (genero == 'Horror' or genero == 'Mistery'):
            # if (ano_lancamento == '\\N' or (1990 <= int(ano_lancamento) <= 1999)) and (genero == 'Horror' or genero == 'Mistery'):
            # if (ano_lancamento == '\\N' or (2000 <= int(ano_lancamento) <= 2009)) and (genero == 'Horror' or genero == 'Mistery'):
            # if (ano_lancamento == '\\N' or (2010 <= int(ano_lancamento) <= 2022)) and (genero == 'Horror' or genero == 'Mistery'):
                url = f'https://api.themoviedb.org/3/movie/{id_filme}?api_key={chave_api}'
                response = requests.get(url)

                if response.status_code == 200 and response.json():
                    dados_filme = response.json()
                    dados_filtrados = {key: dados_filme[key] for key in ["genres", "id", "imdb_id", "original_language",
                                                                        "original_title", "overview", "popularity", "release_date",
                                                                        "revenue", "runtime", "status", "title", "video",
                                                                        "vote_average", "vote_count"] if key in dados_filme}

                    
                    if ano_lancamento == '\\N':
                        s3_path = f'Raw/TMDB/JSON/Movies/{data_atual}/unknown-year/{id_filme}.json'
                    else:
                        s3_path = f'Raw/TMDB/JSON/Movies/{data_atual}/{ano_lancamento}/{id_filme}.json'

                    
                    s3.put_object(Body=json.dumps(dados_filtrados), Bucket=bucket, Key=s3_path)

def lambda_handler(event, context):
    chave_api = '********************************'
    data_atual = datetime.utcnow().strftime("%Y/%m/%d")
    bucket = 'data-lake-diane-nascimento-castedo'
    file_path = 'Raw/Local/CSV/Movies/2023/07/24/movies.csv'
    #file_path = 'Raw/Local/CSV/Movies/2023/07/24/series.csv'
    s3 = boto3.client('s3')

    try:
        
        arquivo_csv = s3.get_object(Bucket=bucket, Key=file_path)
        conteudo_csv = arquivo_csv['Body'].read().decode('utf-8')

        
        registros = list(csv.DictReader(StringIO(conteudo_csv), delimiter='|'))
        tamanho_lote = 100  
        for i in range(0, len(registros), tamanho_lote):
            lote = registros[i:i + tamanho_lote]
            processar_registros(lote, chave_api, s3, bucket, data_atual)

        return {
            'statusCode': 200,
            'body': 'Dados processados e salvos no S3 com sucesso.'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Erro ao processar e salvar os dados no S3: {str(e)}'
        }
