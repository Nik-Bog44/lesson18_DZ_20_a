import pytest
from unittest.mock import MagicMock

from dao.movie import Movie
from dao.movie import MovieDAO
from model.director import Director
from model.genre import Genre
from service.movie import MovieService


@pytest.fixture()
def movie_dao_fixture():
    movie_dao = MovieDAO(None)

    d1 = Director(id=1, name='test')
    g1 = Genre(id=1, name='test')

    red = Movie(id=1,
                title='BLU',
                description='tec tec tec',
                trailer='test',
                year=2023, genre_id=1,
                director_id=1,
                genre=g1,
                director=d1,
                )

    movie_dao.get_one = MagicMock(return_value=red)
    movie_dao.get_all = MagicMock(return_value=[red])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def setup_movie_service(self, movie_dao_fixture):
        self.movie_service = MovieService(dao=movie_dao_fixture)

    def test_partially_update(self):
        movie_d = {
            'id': 1,
            'year': 2021,
        }
        updated_movie = self.movie_service.partially_update(movie_d)

        assert updated_movie.year == 2021

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id == 1

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert movies is not None
        assert len(movies) == 1

    def test_create(self):
        movie_data = {
            'name': 'Rossini',
        }
        movie = self.movie_service.create(movie_data)

        assert movie.id is not None

    def test_update(self):
        movie_data = {
            'id': 1,
            'name': 'Rossini',
        }
        self.movie_service.update(movie_data)

    def test_delete(self):
        self.movie_service.delete(1)
