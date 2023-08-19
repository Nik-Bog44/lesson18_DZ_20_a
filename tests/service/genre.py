import pytest
from unittest.mock import MagicMock

from dao.genre import Genre
from dao.genre import GenreDAO
from service.genre import GenreService


@pytest.fixture()
def genre_dao_fixture():
    genre_dao = GenreDAO(None)

    jon = Genre(id=1)
    olia = Genre(id=2)

    genre_dao.get_one = MagicMock(return_value=jon)
    genre_dao.get_all = MagicMock(return_value=[jon, olia])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def setup_genre_service(self, genre_dao_fixture):
        self.genre_service = GenreService(dao=genre_dao_fixture)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.id == 1

    def test_get_all(self):
        genres = self.genre_service.get_all()

        assert genres is not None
        assert len(genres) == 2

    def test_create(self):
        genre_id = {
            'id': 3,
        }
        genre = self.genre_service.create(genre_id)

        assert genre.id is not None

    def test_update(self):
        genre_id = {
            'id': 5,
        }
        self.genre_service.update(genre_id)

    def test_delete(self):
        self.genre_service.delete(1)
