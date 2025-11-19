# Backend — Projeto Pet

Este diretório contém a API em Flask usada pelo Projeto Pet.

Requisitos

- Python 3.8+
- Instale dependências:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Rodando localmente

```bash
cd backend
# inicializa o banco (se necessário)
python seed_db.py
# rodar app
python app.py
# A API ficará disponível em http://127.0.0.1:5000
```

Documentação
- OpenAPI/Swagger: `backend/swagger.yaml` (o Swagger UI pode ser servido pelo backend em `/swagger` se habilitado).

Notas
- O banco é um arquivo SQLite em `backend/instance/site.db` (não rastreado no Git). Já fizemos backup deste arquivo antes de limpar o histórico.
# Pet Web — Backend (API)

Backend em Python usando Flask e Flask-SQLAlchemy. Fornece endpoints para gerenciar usuários, raças e cachorros.

Pré-requisitos
- Python 3.10+ (ou 3.8+)
- Instalar dependências:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Inicialização local
1. Criar a pasta `instance/` (o script `seed_db.py` já garante isso). Exemplo:

```bash
mkdir -p backend/instance
```

2. Popular banco de dados com raças de exemplo:

```bash
python backend/seed_db.py
```

3. Rodar o servidor Flask:

```bash
python backend/app.py
# ou, usando a fábrica de app via FLASK_APP:
export FLASK_APP=backend/app.py
flask run --port 5000
```

Principais rotas para demonstração (4 exigidas pelo trabalho)
- `GET /racas` — lista todas as raças
- `GET /usuarios/email/{email}` — busca usuário por e-mail (uso no fluxo de login leve)
- `POST /usuarios` — cria usuário (ex: para cadastro)
- `POST /cachorros` — cria cachorro associado a `user_id` e `raca_id` (ex: registrar pet)

Documentação OpenAPI/Swagger
- Acesse a UI Swagger em: `http://127.0.0.1:5000/swagger`
- O arquivo `backend/swagger.yaml` contém a especificação completa das rotas.

Notas para o vídeo
- Explique o fluxo: `seed_db.py` cria/insere raças; `app.py` é a fábrica de app com as rotas e serve o frontend; `database.py` contém os modelos e relações (User 1->N Cachorro). Mostre exemplos de payload no Swagger "Try it out".

Separando repositórios
- Para enviar aos professores, crie dois repositórios no GitHub: um para `backend/` e outro para `frontend/`. Inclua nestes repositorios os READMEs correspondentes.
