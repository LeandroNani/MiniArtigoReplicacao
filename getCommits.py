import requests
import json

usuario = "LeandroNani"  # Seu nome de usuário do GitHub
token = ""  # Seu token de acesso pessoal

commits_url = 'https://api.github.com/repos/microsoft/vscode/commits?per_page=100'
api = requests.get(commits_url, auth=(usuario, token))
dados_api = api.json()

total_commits = len(dados_api)  # Inicializa o contador de commits
pagina_atual = 1  # Inicializa o contador de páginas

# para pegar 10000 commits
while 'next' in api.links and total_commits < 10000:
    pagina_atual += 1
    print(f"Buscando página {pagina_atual}...")
    next_page_url = api.links['next']['url']
    api = requests.get(next_page_url, auth=(usuario, token))

    if api.status_code == 200:
        new_commits = api.json()
        dados_api.extend(new_commits)
        total_commits += len(new_commits)
    else:
        print("Erro na requisição à API:", api.status_code)
        break


with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(dados_api, f, ensure_ascii=False, indent=4)

print(f"Total de commits coletados: {total_commits}")