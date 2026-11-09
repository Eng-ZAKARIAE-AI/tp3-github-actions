# Exercice 1 : frais de livraison
def frais_livraison(montant):
    if montant < 0:
        raise ValueError("Montant negatif")
    if montant >= 300:
        return 0
    return 25


def calculer_delai_livraison(zone, express=False):
    """Calcule le délai de livraison en jours selon la zone."""
    if zone == "locale":
        return 1 if express else 3
    elif zone == "nationale":
        return 2 if express else 5
    elif zone == "internationale":
        return 5 if express else 10
    else:
        raise ValueError(f"Zone inconnue: {zone}")


def est_livraison_gratuite(montant, client_premium=False):
    """Détermine si la livraison est gratuite."""
    if client_premium:
        return True
    return montant >= 300