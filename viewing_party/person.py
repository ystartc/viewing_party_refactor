from viewing_party.movie import Movie

class Person:
    def __init__(self, name, friends = None):
        self.name = name
        self.friends = [] if friends is None else friends
        self.watchlist = []
        self.watched = []

    def add_friend(self, new_friend):
        if new_friend not in self.friends:
            self.friends.append(new_friend)

    def add_movie_to_watchlist(self, new_movie):
        if new_movie not in self.watchlist:
            self.watchlist.append(new_movie)
    
    def add_movie_to_watched(self, movie):
        if movie not in self.watched:
            self.watched.append(movie)
        if movie in self.watchlist:
            self.watchlist.remove(movie)