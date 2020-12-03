import unittest
from app.models import Movie

class MovieTest(unittest.TestCase):
    """
    test class to test the behaviour of the movie classs
    """
    def setUp(self):
        """
        set up method that will run before every test
        """
        self.new_movie = Movie(1234, 'Python must be Crazy', 'A thrilling new Python Series', 'https://image.tmdb.org/t/p/w500/khsjha27hbs', 8.5, 129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie, Movie))

