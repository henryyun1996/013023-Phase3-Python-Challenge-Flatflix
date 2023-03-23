class Viewer:
    all = []
    def __init__(self, username):
        if username not in Viewer.all:
            if (type(username) == str and 6 <= len(username) <= 16):
                self._username = username
                self.reviews = []
                self.reviewed_movies = []
                Viewer.all.append(username)
            else:
                raise Exception("Please use string for username and keep it between 6 and 16 characters.") 
        else:
            raise Exception("Username must be unique")
        
    
    
    def get_username(self):
        return self._username
    def set_username(self, username):
        if (type(username) == str and 6 <= len(username) <= 16):
            self._username = username

    def add_review(self, review):
        self.reviews.append(review)

    def add_movie(self, movie):
        if (not self.reviewed_movie(movie)):
            self.reviewed_movies.append(movie)

    username = property(get_username, set_username)

    def reviewed_movie(self, movie):
        if (movie in self.reviewed_movies):
            return True
        else:
            return False


    def rate_movie(self, movie, rating):
        from .review import Review
        if (movie in self.reviewed_movies):
            for review in self.reviews:
                if (review.movie == movie):
                    review.set_rating(rating)
        else:
            Review(self, movie, rating)