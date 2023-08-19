import pytest
from unittest.mock import MagicMock

from dao.director import Director
from dao.director import DirectorDAO
from service.director import DirectorService


@pytest.fixture()
def director_dao_fixture():
    director_dao = DirectorDAO(None)

    jon = Director(id=1, name='Jon')
    olia = Director(id=2, name='Olia')

    director_dao.get_one = MagicMock(return_value=jon)
    director_dao.get_all = MagicMock(return_value=[jon, olia])  # Corrected return value
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def setup_director_service(self, director_dao_fixture):
        self.director_service = DirectorService(dao=director_dao_fixture)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id == 1

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert directors is not None
        assert len(directors) == 2

    def test_create(self):
        director_id = {
            'name': 'Rossini',
        }
        director = self.director_service.create(director_id)

        assert director.id is not None

    def test_update(self):
        director_id = {
            'id': 1,
            'name': 'Rossini',
        }
        self.director_service.update(director_id)

    def test_delete(self):
        self.director_service.delete(1)
