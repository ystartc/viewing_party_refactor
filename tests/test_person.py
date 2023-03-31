from viewing_party.person import Person

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
