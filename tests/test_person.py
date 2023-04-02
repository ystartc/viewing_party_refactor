from viewing_party.person import Person
from viewing_party.movie import Movie

import pytest

def test_creating_person_initializes_instance_variables():
    # Arrange / Act
    kendall = Person("Kendall")

    # Assert
    assert kendall.name == "Kendall"
    assert kendall.friends == []

def test_adding_friend_multiple_times_does_not_create_duplicate():
    # Arrange
    kendall = Person("Kendall")
    simon = Person("Simon")

    # Act
    kendall.add_friend(simon)
    kendall.add_friend(simon)

    # Assert
    assert kendall.friends == [simon]

def test_adding_movie_multiple_times_does_not_create_duplicate():
    # Arrange
    movie = Movie("Redemption", "Action", 8)
    person = Person('Angie')
    
    # Act
    person.add_movie_to_watchlist(movie)
    person.add_movie_to_watchlist(movie)

    # Assert
    assert person.watchlist == [movie]
    
def test_adding_movie_to_watched_list_does_not_create_dublicate():
    # Arrange
    movie = Movie("Doctor Strange", "Action", 10)
    person = Person('Clark')
    
    # Act
    person.add_movie_to_watched(movie)
    person.add_movie_to_watched(movie)

    # Assert
    assert person.watched == [movie]
    assert len(person.watched) == 1
    
def test_adding_movie_to_watched_removes_it_from_watchlist():
    # Arrange
    movie = Movie("Naruto", "Anime", 8)
    person = Person('Aman')
    
    # Act
    person.add_movie_to_watchlist(movie)
    person.add_movie_to_watched(movie)

    # Assert
    assert person.watched == [movie]
    assert len(person.watched) == 1
    assert movie not in person.watchlist
    
def test_watchlist_remain_the_same_when_adding_movie_to_watched_if_was_not_in_watchlist():
    # Arrange
    movie = Movie("Harry Potter", "Fantasy", 10)
    movie2 = Movie("Naruto", "Anime", 8)
    person = Person('Ronald')
    
    # Act
    person.add_movie_to_watchlist(movie2)
    person.add_movie_to_watched(movie)

    # Assert
    assert person.watched == [movie]
    assert len(person.watched) == 1
    assert person.watchlist == [movie2]
    assert len(person.watchlist) == 1