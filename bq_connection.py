from google.cloud import bigquery
from google.oauth2 import service_account
from yaml_reader import read_config
config = read_config('config/config.yaml')

project_id = config['project_id']
credentials = service_account.Credentials.from_service_account_file(config['credentials_path'])
client = bigquery.Client(credentials=credentials, project=project_id)

def titles (self) -> list(str):
    query = f"""
            SELECT title
            FROM `{project_id}.dev.cleaned_books`
            """
    # print(query)
    rows = client.query(query=query).result()
    title_list = list()
    for r in rows:
        title_list.append(list(r.values()))
    print(title_list)


