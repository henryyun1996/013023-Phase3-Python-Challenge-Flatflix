from .viewer import Viewer
from .movie import Movie

class Review:
    
   def __init__(self, viewer, movie, rating):
        if (isinstance(viewer, Viewer)):
           self._viewer = viewer
        else:
           raise Exception('invalid viewer')
           
        if (isinstance(movie, Movie)):
           self._movie = movie
        else:
           raise Exception('invalid movie')
        if (type(rating) == int and 1 <= rating <= 5):
           self._rating = rating
        else:
           raise Exception("please use rating between 1 and 5, inclusive")
        
        movie.add_review(self)
        viewer.add_review(self)
        viewer.add_movie(movie)
        

   
   def get_rating(self):
      return self._rating
   def set_rating(self, rating):
      if (type(rating) == int and 1 <= rating <= 5):
         self._rating = rating
    
   rating = property(get_rating, set_rating)

   def get_viewer(self):
      return self._viewer
   def set_viewer(self, viewer):
      self._viewer = viewer

   viewer = property(get_viewer, set_viewer)

   def get_movie(self):
      return self._movie
   def set_movie(self, movie):
      self._movie = movie

   movie = property(get_movie, set_movie)
