import boto3
import pandas as pd
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

nome_bucket = 'data-lake-do-marcos'
raw_zone = 'Raw'
origem = 'file'
formato = 'CSV'
data = datetime.now().strftime('%Y/%m/%d')

local_files = {
    'Movies': '/app/data/movies.csv',
    'Series': '/app/data/series.csv'
}

def upload_to_s3(local_path, category):
    try:
        df = pd.read_csv(local_path, delimiter='|', low_memory=False)
        
        s3_path = f"{raw_zone}/{origem}/{formato}/{category}/{data}/{os.path.basename(local_path)}"
        
        s3 = boto3.client(
            's3',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            aws_session_token=os.getenv('AWS_SESSION_TOKEN'),
            region_name=os.getenv('AWS_DEFAULT_REGION')
        )
        s3.put_object(Bucket=nome_bucket, Key=s3_path, Body=df.to_csv(index=False))
        
        print(f"Arquivo {local_path} carregado para {s3_path} no bucket {nome_bucket}")
    except Exception as e:
        print(f"Erro ao carregar o arquivo {local_path}: {e}")

if __name__ == "__main__":
    for category, local_path in local_files.items():
        upload_to_s3(local_path, category)
