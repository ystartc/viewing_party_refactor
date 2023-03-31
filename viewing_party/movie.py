class Movie:
    def __init__(self, name, genre, rating):
        self.name = name
        self.genre = genre
        self.rating = rating
        self.watchlist = []

    def add_movie_to_watchlist(self, new_movie):
        if new_movie not in self.watchlist:
            self.watchlist.append(new_movie)
    
    