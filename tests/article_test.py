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
        self.new_article = Article('source','http://img.com','doe', 'article','some article', '2018-05-12T13:31:03Z', 'bbc.com')

    def test_init(self):
        '''
        test if object is instantiated correctly
        '''
        self.assertEqual(self.new_article.source, "source")
        self.assertEqual(self.new_article.urlToImage, "http://img.com")
        self.assertEqual(self.new_article.author, "doe")
        self.assertEqual(self.new_article.title, "article")
        self.assertEqual(self.new_article.description, "some article")
        self.assertEqual(self.new_article.publishedAt, "2018-05-12T13:31:03Z")
        self.assertEqual(self.new_article.ulr, "bbc.com")
