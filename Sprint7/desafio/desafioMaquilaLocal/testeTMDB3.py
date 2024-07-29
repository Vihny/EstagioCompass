import os
import json
import requests
import boto3
from dotenv import load_dotenv
from datetime import datetime

# Carregar variáveis do arquivo .env
load_dotenv()

# Configuração do cliente S3
s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    aws_session_token=os.getenv('AWS_SESSION_TOKEN'),
    region_name=os.getenv('AWS_DEFAULT_REGION')
)

bucket_name = os.getenv('BUCKET_NAME')
tmdb_api_key = os.getenv('TMDB_API_KEY')


GENRE_ANIMATION_ID = 16  # ID do gênero de animação

def fetch_movies_by_genre(genre_id):
    data = []
    page = 1
    max_pages = 500  # Máximo permitido pela API
    base_url = "https://api.themoviedb.org/3/discover/movie"
    
    while page <= max_pages:
        print(f"Buscando filmes - Página {page}...")
        response = requests.get(
            base_url,
            params={
                'api_key': tmdb_api_key,
                'with_genres': genre_id,
                'sort_by': 'popularity.desc',
                'page': page,
                'vote_average.gte': 8,  # Filtra filmes com nota média maior ou igual a 8
                'primary_release_date.gte': '2010-01-01',  # Data de lançamento a partir de 2010
                'primary_release_date.lte': '2020-12-31'  # Data de lançamento até 2020
            }
        )
        if response.status_code != 200:
            raise Exception(f"Erro ao buscar dados: {response.status_code} - {response.text}")
        
        results = response.json().get('results', [])
        if not results:
            break
        
        for m in results:
            movie_id = m['id']
            movie_details = fetch_movie_details(movie_id)
            title = movie_details.get('title', 'Unknown')
            production_countries = movie_details.get('production_countries', [])
            countries = [country['name'] for country in production_countries]
            revenue = movie_details.get('revenue', 'Unknown')
            
            data.append({
                'id': movie_id,
                'title': title,
                'countries_of_origin': countries,
                'revenue': revenue
            })
        
        page += 1

    return data

def fetch_movie_details(movie_id):
    base_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    response = requests.get(
        base_url,
        params={'api_key': tmdb_api_key}
    )
    if response.status_code != 200:
        raise Exception(f"Erro ao buscar detalhes do filme: {response.status_code} - {response.text}")
    
    return response.json()

def save_to_s3(data, category):
    date_str = datetime.now().strftime('%Y/%m/%d')
    base_file_name = f"tmdb_{category}_data_{int(datetime.now().timestamp())}"
    
    def chunk_data(data, chunk_size):
        for i in range(0, len(data), chunk_size):
            yield data[i:i + chunk_size]
    
    # Divide os dados em chunks de 100 registros para garantir que cada arquivo tenha no máximo 100 registros
    chunk_size = 100
    data_chunks = list(chunk_data(data, chunk_size))

    for idx, chunk in enumerate(data_chunks):
        file_name = f"{base_file_name}_part_{idx + 1}.json"
        s3_path = f"Raw/TMDB/JSON/{date_str}/{file_name}"
        data_json = json.dumps(chunk, indent=4)
        
        s3_client.put_object(
            Bucket=bucket_name,
            Key=s3_path,
            Body=data_json,
            ContentType='application/json'
        )
        print(f"Arquivo salvo no S3: {s3_path}")

def main():
    try:
        animation_data = fetch_movies_by_genre(GENRE_ANIMATION_ID)
        if animation_data:
            save_to_s3(animation_data, 'Animation')
        else:
            print("Nenhum dado de filmes de animação encontrado.")
        
        print('Dados coletados e enviados para o S3')
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()

