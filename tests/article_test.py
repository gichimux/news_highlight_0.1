import unittest
from app.models import Article

class TestArticle(unittest.TestCase):
    '''
    test the behaviour of the article class
    '''
    
    def setUp(self):
        '''
        test that will run before every test
        '''
        self.new_article = Article()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article 