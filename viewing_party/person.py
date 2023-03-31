from viewing_party.movie import Movie

class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.watchlist = []

    def add_friend(self, new_friend):
        if new_friend not in self.friends:
            self.friends.append(new_friend)

    def add_movie_to_watchlist(self, new_movie):
        if new_movie not in self.watchlist:
            self.watchlist.append(new_movie)