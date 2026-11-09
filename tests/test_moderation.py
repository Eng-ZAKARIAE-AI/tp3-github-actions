# Exercice 4 - tests d'isolation des dependances
from unittest.mock import Mock

import pytest

from app.moderation import decider


def test_decider_bloque_un_spam():
    modele = Mock()
    modele.predict.return_value = "spam"

    assert decider(modele, "Offre miracle") == "bloquer"
    modele.predict.assert_called_once_with("Offre miracle")


def test_decider_autorise_un_message_normal():
    modele = Mock()
    modele.predict.return_value = "normal"

    assert decider(modele, "Bonjour") == "autoriser"
    modele.predict.assert_called_once_with("Bonjour")


def test_decider_propage_erreur_du_modele():
    modele = Mock()
    modele.predict.side_effect = RuntimeError("Modele indisponible")

    with pytest.raises(RuntimeError, match="Modele indisponible"):
        decider(modele, "Offre miracle")