# Pet Web - Full Stack SPA Project

Este é um projeto Full Stack desenvolvido como uma Single Page Application (SPA) para o "Pet Web", conforme o wireframe gráfico. O objetivo é demonstrar a integração de um backend em Python (Flask) com um frontend interativo (HTML, CSS, JavaScript), utilizando Pydantic para validação de dados e Flask-OpenAPI3 para documentação de API (Swagger UI).
Tecnologias Utilizadas

## Backend:

    Python 3
    Flask: Microframework web
    Flask-OpenAPI3: Integração OpenAPI/Swagger UI com Flask e Pydantic
    Pydantic: Validação de dados (modelos para requests/responses)
    SQLite3: Banco de dados relacional leve
    <img width="916" height="744" alt="grafik" src="https://github.com/user-attachments/assets/a72ea245-c030-483a-951f-49704ba59ac5" />


## Frontend:

    HTML5: Estrutura da página
    CSS3: Estilização responsiva
    JavaScript (ES6+): Interatividade SPA, manipulação do DOM, requisições Fetch API para o backend

Pré-requisitos
Certifique-se de ter o Python 3 e o pip (gerenciador de pacotes do Python) instalados em seu sistema. O SQLite3 geralmente vem pré-instalado com o Python e no macOS.

# Backend — Projeto Pet
## Estrutura recomendada para instalação- como fica apos a instalação :
<img width="1638" height="209" alt="grafik" src="https://github.com/user-attachments/assets/af59ee4f-4feb-4ef8-bad4-2762818f0149" />


## Este diretório contém a API em Flask usada pelo Projeto Pet.

### Requisitos
- Crie um ambiente virtual (recomendado)
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
# inicializa o banco (se necessário- se ainda não existe)
python seed_db.py
# rodar app
python app.py
# A API ficará disponível em http://127.0.0.1:5000
```

Documentação
- OpenAPI/Swagger: `backend/swagger.yaml` (o Swagger UI pode ser servido pelo backend em `/swagger` se habilitado).

Notas
- O banco é um arquivo SQLite em `backend/instance/site.db
<img width="916" height="744" alt="grafik" src="https://github.com/user-attachments/assets/8a186726-e2ee-459b-845a-6a458b49e1ec" />


  
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
- Explica o fluxo: `seed_db.py` cria/insere raças; `app.py` é a fábrica de app com as rotas e serve o frontend; `database.py` contém os modelos e relações (User 1->N Cachorro). Mostre exemplos de payload no Swagger "Try it out".

Frontend e backend estao em repositórios separando 
