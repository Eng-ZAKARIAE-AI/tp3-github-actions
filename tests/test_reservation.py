# Exercice 3 : tests d’intégration des réservations
import pytest

from app.reservation import Reservation, Stock


@pytest.fixture
def stock():
    return Stock(5)


def test_reservation_deux_unites_confirmee_et_stock_reduit(stock):
    reservation = Reservation(stock)

    assert reservation.reserver(2) == "confirmee"
    assert stock.quantite == 3


def test_reservation_six_unites_refusee_et_stock_inchange(stock):
    reservation = Reservation(stock)

    assert reservation.reserver(6) == "refusee"
    assert stock.quantite == 5


def test_reservation_cinq_unites_confirmee_et_stock_vide(stock):
    reservation = Reservation(stock)

    assert reservation.reserver(5) == "confirmee"
    assert stock.quantite == 0


def test_reservation_zero_unite_leve_value_error_et_stock_inchange(stock):
    reservation = Reservation(stock)

    with pytest.raises(ValueError):
        reservation.reserver(0)

    assert stock.quantite == 5