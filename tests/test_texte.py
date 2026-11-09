# Exercice 2 : tests de nettoyage de texte
import pytest

from app.texte import nettoyer_texte


@pytest.mark.parametrize(
    "entree, attendu",
    [
        ("  BONJOUR   monde  ", "bonjour monde"),
        (" déjà propre ", "déjà propre"),
        ("", ""),
        ("   ", ""),
        (" PYTHON ", "python"),
    ],
)
def test_nettoyer_texte(entree, attendu):
    assert nettoyer_texte(entree) == attendu


@pytest.mark.parametrize("entree", [123, None])
def test_nettoyer_texte_entree_non_textuelle(entree):
    with pytest.raises(TypeError):
        nettoyer_texte(entree)


def test_nettoyer_texte_deja_nettoye_ne_change_pas():
    texte_nettoye = nettoyer_texte("  BONJOUR   monde  ")
    assert nettoyer_texte(texte_nettoye) == texte_nettoye