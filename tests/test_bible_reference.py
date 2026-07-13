import pytest
from pydantic import ValidationError

from emmaus_engine.bible.models import BibleReference


def test_affiche_un_verset_unique() -> None:
    reference = BibleReference(
        book="Romains",
        chapter=8,
        verse_start=1,
    )

    assert reference.display() == "Romains 8:1"


def test_affiche_une_plage_de_versets() -> None:
    reference = BibleReference(
        book="Jacques",
        chapter=1,
        verse_start=2,
        verse_end=4,
    )

    assert reference.display() == "Jacques 1:2-4"


def test_refuse_une_plage_inversee() -> None:
    with pytest.raises(ValidationError):
        BibleReference(
            book="Jean",
            chapter=3,
            verse_start=16,
            verse_end=15,
        )
