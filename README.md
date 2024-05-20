# SteamDB Sales Scraper

O projeto tem por objetivo extrair dados de promoções do site SteamDB e armazená-los no Google BigQuery para posterior visualização e análise.

## Estrutura do Projeto

- `scraper.py`: Script responsável por realizar a raspagem dos dados de promoções do site SteamDB.
- `bigquery_upload.py`: Script para enviar os dados raspados para o Google BigQuery.
- `requirements.txt`: Lista de dependências necessárias para executar os scripts.

## Requisitos

- Python 3.8+
- Conta no Google Cloud Platform com acesso ao BigQuery
- Credenciais do Google Cloud para autenticação

## Configuração

1. Clone este repositório:

    ```bash
    git clone https://github.com/seuusuario/steamdb-sales-scraper.git
    cd steamdb-sales-scraper
    ```

2. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure suas credenciais do Google Cloud:

    - Crie um novo projeto no [Google Cloud Console](https://console.cloud.google.com/).
    - Habilite a API do BigQuery.
    - Crie uma conta de serviço e baixe o arquivo JSON das credenciais.
    - Defina a variável de ambiente `GOOGLE_APPLICATION_CREDENTIALS` para apontar para o arquivo JSON:

      ```bash
      export GOOGLE_APPLICATION_CREDENTIALS="path/to/credentials.json"
      ```

## Execução

1. Execute o script de raspagem para obter os dados de promoções do SteamDB:

    ```bash
    python scraper.py
    ```

2. Envie os dados raspados para o Google BigQuery:

    ```bash
    python bigquery_upload.py
    ```

## Visualização dos Dados

Os dados podem ser visualizados diretamente no Google BigQuery, exportados para um Google Sheets ou Google Data Studio.

### Link no Google Sheets e Google Data Studio

<!-- 1. [Google Sheets](https://docs.google.com/spreadsheets/d/e/2PACX-1vSA7wehUbLUoav79bJbNoSRczZiDtufYtRlomfQjvWTqO5xZ_0NNh6HpHEWUZdeNhm3vdGwAub1hMck/pubhtml) -->

1. <a href="https://docs.google.com/spreadsheets/d/e/2PACX-1vSA7wehUbLUoav79bJbNoSRczZiDtufYtRlomfQjvWTqO5xZ_0NNh6HpHEWUZdeNhm3vdGwAub1hMck/pubhtml" target="_blank">Google Sheets</a>

2. <a href="https://lookerstudio.google.com/reporting/7c18a400-aa79-46a2-afdc-f96b35fc63da" target="_blank">Google Data Studio</a>

## Arquitetura da Solução

1. **Raspagem dos Dados:** O script `scraper.py` utiliza bibliotecas como `requests` e `BeautifulSoup` para extrair informações de promoções do SteamDB.
2. **Armazenamento no BigQuery:** O script `bigquery_upload.py` utiliza a biblioteca `google-cloud-bigquery` para enviar os dados extraídos para uma tabela específica no BigQuery.
3. **Visualização no Google Sheets:** Os dados no BigQuery podem ser conectados ao Google Sheets para criar visualizações dinâmicas.
