#!/usr/bin/env bash
set -euo pipefail
# Script para iniciar o backend localmente (venv + install + run)
# Uso:
#   chmod +x backend/run_backend.sh
#   ./backend/run_backend.sh

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

# Cria venv se não existir
if [ ! -d ".venv" ]; then
  echo "Criando ambiente virtual .venv..."
  python3 -m venv .venv
fi

# Ativa o venv
# shellcheck source=/dev/null
source .venv/bin/activate

echo "Instalando dependências do backend (requirements.txt)..."
pip install --upgrade pip >/dev/null
pip install -r backend/requirements.txt

# Garante que a pasta instance exista
mkdir -p backend/instance

echo "Iniciando o servidor Flask (backend/app.py)..."
exec python backend/app.py
