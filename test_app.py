from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_health():
    reponse = client.get("/health")
    assert reponse.status_code == 200
    assert reponse.json() == {"status": "ok"}


def test_ask_sans_cle_renvoie_erreur(monkeypatch):
    # Sans clé d'API, le service doit répondre proprement par une erreur 500.
    monkeypatch.delenv("DEEPSEEK_API_KEY", raising=False)
    reponse = client.post("/ask", json={"question": "Bonjour"})
    assert reponse.status_code == 500
    assert "DEEPSEEK_API_KEY" in reponse.json()["detail"]


def test_ask_corps_invalide():
    # Le corps de la requête doit contenir le champ "question".
    reponse = client.post("/ask", json={})
    assert reponse.status_code == 422
