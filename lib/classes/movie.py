import statistics

class Movie:

    all = []

    def __init__(self, title):
        if (type(title) == str and len(title) > 0):
            self._title = title
            self.reviews = []
            self.reviewers = []
            Movie.all.append(self)
        else:
            raise Exception("Use a string for title and use a title longer than 0 characters.")

    def get_title(self):
        return self._title
    def set_title(self, title):
        if (type(title) == str and len(title) > 0):
            self._title = title

    title = property(get_title, set_title)

    def add_review(self, review):
        self.reviews.append(review)
    def average_rating(self):
        return statistics.mean([review.get_rating() for review in self.reviews])

    @classmethod
    def highest_rated(cls):
        countobject = {}
    
        for movie in cls.all:
            countobject[movie] = movie.average_rating()

        return max(countobject, key = countobject.get)




