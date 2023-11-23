import boto3
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION")
BUCKET_NAME = 'data-lake-diane-nascimento-castedo'
movies_file_path = '/app/data/movies.csv'

def send_to_s3(file_path, data_type):
    try:
        s3 = boto3.resource('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

        date_processed = datetime.now().strftime("%Y/%m/%d")

        s3_path = f"{BUCKET_NAME}/Raw/Local/CSV/{data_type}/{date_processed}/{os.path.basename(file_path)}"

        s3.Bucket(BUCKET_NAME).upload_file(file_path, s3_path)
        print(f"{file_path} enviado para o S3 em {s3_path}")
        return True
    except Exception as e:
        print(f"Erro ao enviar {file_path} para o S3: {e}")
        return False

if send_to_s3(movies_file_path, 'Movies'):
    print("Arquivo de filmes enviado com sucesso!")
else:
    print("Falha ao enviar o arquivo de filmes!")

# if send_to_s3(series_file_path, 'Series'):
#     print("Arquivo de séries enviado com sucesso!")
# else:
#     print("Falha ao enviar o arquivo de séries!")
