""" 
References:
https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv
https://googleapis.dev/python/google-api-core/latest/exceptions.html
https://cloud.google.com/bigquery/docs/loading-data-local
https://cloud.google.com/bigquery/docs/loading-data
https://cloud.google.com/bigquery/docs/loading-data-local#loading_data_from_a_local_file
"""

import os
from google.cloud import bigquery
from google.api_core.exceptions import GoogleAPIError
from typing import NoReturn

def configure_bigquery_client(service_account_json: str) -> bigquery.Client:
    """Configura e retorna um cliente BigQuery."""
    try:
        client = bigquery.Client.from_service_account_json(service_account_json)
        return client
    except GoogleAPIError as e:
        raise RuntimeError(f"Falha ao configurar o cliente do BigQuery: {e}")

def load_csv_to_bigquery(client: bigquery.Client, dataset_id: str, table_id: str, csv_file_path: str) -> NoReturn:
    """Carrega dados de um arquivo CSV para uma tabela BigQuery."""
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        autodetect=True,
        skip_leading_rows=1
    )

    table_ref = client.dataset(dataset_id).table(table_id)

    try:
        with open(csv_file_path, 'rb') as source_file:
            job = client.load_table_from_file(source_file, table_ref, job_config=job_config)
        job.result()  # Aguardar a conclusão do job
        print(f'Tabela {table_id} carregada com sucesso no dataset {dataset_id}.')
    except (FileNotFoundError, GoogleAPIError) as e:
        raise RuntimeError(f"Falha ao carregar CSV no BigQuery: {e}")

def main() -> NoReturn:
    """Caminho do arquivo JSON de credenciais."""
    service_account_json = os.getenv('GOOGLE_APPLICATION_CREDENTIALS', '/Users/nameuser/Folder/my-project-1.json')
    dataset_id = 'steamdb'
    table_id = 'steamdb_sales'
    csv_file_path = 'steam_sales.csv'

    client = configure_bigquery_client(service_account_json)
    load_csv_to_bigquery(client, dataset_id, table_id, csv_file_path)

if __name__ == "__main__":
    main()
