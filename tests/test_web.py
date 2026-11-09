import pytest

from app.web import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_moderate_autorise_message_normal(client):
    response = client.post("/moderate", json={"message": "bonjour"})

    assert response.status_code == 200
    assert response.get_json() == {"decision": "autoriser"}


def test_moderate_bloque_message_contenant_spam_sans_casse(client):
    response = client.post("/moderate", json={"message": "ceci est du SPAM"})

    assert response.status_code == 200
    assert response.get_json() == {"decision": "bloquer"}


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"message": 42},
        {"message": "   "},
    ],
)
def test_moderate_refuse_message_invalide(client, payload):
    response = client.post("/moderate", json=payload)

    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid message"}


def test_moderate_refuse_corps_json_qui_n_est_pas_un_objet(client):
    response = client.post("/moderate", json=["message", "bonjour"])

    assert response.status_code == 400
    assert response.get_json() == {"error": "JSON object required"}
