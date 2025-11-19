# Verificação e Evidências — Backend

Este arquivo descreve comandos práticos para validar localmente que o backend e o Swagger estão funcionando e que os exemplos foram adicionados ao `swagger.yaml`.

1) Preparar ambiente e popular DB

```bash
cd /Users/elainebundscherer/ONE/projeto_pet_web
python -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
python backend/seed_db.py
```

2) Rodar servidor

```bash
python backend/app.py
# ou
export FLASK_APP=backend/app.py
flask run --port 5000
```

3) Comandos de verificação rápidos

```bash
# Verificar que o Swagger YAML está sendo servido
curl -s http://127.0.0.1:5000/swagger.yaml | sed -n '1,80p'

# Verificar presença de blocos 'examples:' no YAML
curl -s http://127.0.0.1:5000/swagger.yaml | grep -n "examples:"

# Checar a rota /racas (deve retornar JSON - lista ou [])
curl -s http://127.0.0.1:5000/racas | jq .
```

4) Saída esperada (exemplos)

- O `curl` para `swagger.yaml` deve conter trechos similares a:

```yaml
responses:
  200:
    description: Uma lista de objetos de raça.
    schema:
      type: array
      items:
        $ref: '#/definitions/Raca'
    examples:
      application/json:
        - id: 1
          nome: "Labrador Retriever"
          porte: "Grande"
          grupo: "Companhia"
```

- O `curl` para `/racas` pode retornar `[]` ou uma lista JSON com raças, dependendo se o `seed_db.py` foi executado.

Observação: se preferir, eu posso executar esses comandos aqui no workspace e enviar as saídas capturadas. Confirme se quer que eu rode o servidor e valide automaticamente.
