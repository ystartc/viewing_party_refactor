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

def test_adding_movie_multiple_times_does_not_create_duplicate():
    # Arrange
    
    movie = Movie("Redemption", "Action", 8)
    person = Person('Angie')
    
    # Act
    person.add_movie_to_watchlist(movie)
    person.add_movie_to_watchlist(movie)

    # Assert
    assert movie.watchlist == [movie]