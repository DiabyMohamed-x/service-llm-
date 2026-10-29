# Projet LLM

Petit service FastAPI qui appelle une API de LLM (DeepSeek, format compatible OpenAI).

## Installation

```bash
cd ~/Documents/Claude_Workoud/LLM
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Clé d'API

Crée un fichier `.env` dans ce dossier (il est ignoré par Git) :

```
DEEPSEEK_API_KEY=ta_clé_ici
```

Ne mets jamais la clé dans le code ni dans Git.

## Lancer

```bash
python hello.py                      # premier test en ligne de commande
uvicorn app:app --reload             # service sur http://127.0.0.1:8000
```

Tester le service :

```bash
curl http://127.0.0.1:8000/health
curl -X POST http://127.0.0.1:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "Explique le CI/CD en deux phrases."}'
```

## Docker

```bash
docker build -t service-llm .
docker run --rm -p 8000:8000 -e DEEPSEEK_API_KEY="$DEEPSEEK_API_KEY" service-llm
```

## Tests et CI

```bash
pip install -r requirements-dev.txt
pytest -v
```

La pipeline GitLab CI (`.gitlab-ci.yml`) lance les tests, puis construit l'image Docker
et vérifie que `/health` répond.
