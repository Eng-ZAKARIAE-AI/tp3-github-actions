from unittest.mock import patch

import pytest

from app.notifications import envoyer_notification
from app.surveillance import surveiller


def test_notification_service_leve_runtime_error():
    with pytest.raises(RuntimeError, match="Service non configure"):
        envoyer_notification("Taux eleve")


def test_surveiller_taux_superieur_au_seuil_declenche_alerte():
    with patch("app.surveillance.envoyer_notification") as notifier:
        assert surveiller(0.15) == "alerte"

    notifier.assert_called_once_with("Taux eleve")


def test_surveiller_taux_inferieur_au_seuil_ne_declenche_pas_alerte():
    with patch("app.surveillance.envoyer_notification") as notifier:
        assert surveiller(0.05) == "ok"

    notifier.assert_not_called()


def test_surveiller_taux_egal_au_seuil_ne_declenche_pas_alerte():
    with patch("app.surveillance.envoyer_notification") as notifier:
        assert surveiller(0.10) == "ok"

    notifier.assert_not_called()


def test_surveiller_propage_erreur_du_service_de_notification():
    with patch(
        "app.surveillance.envoyer_notification",
        side_effect=RuntimeError("Service indisponible"),
    ):
        with pytest.raises(RuntimeError, match="Service indisponible"):
            surveiller(0.15)
