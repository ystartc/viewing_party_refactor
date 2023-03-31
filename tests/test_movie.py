import pytest
from viewing_party.movie import Movie
from viewing_party.person import Person

def test_creating_movie_initializes_instance_variables():
    # Arrange/Act
    movie = Movie('Titanic', 'Romance', 10)
    
    # Assert
    assert movie.name == 'Titanic'
    assert movie.genre == 'Romance'
    assert movie.rating == 10
