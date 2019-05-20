import unittest
from app.models import News

class TestSource(unittest.TestCase):
    '''
    test the behaviour of the article class
    '''
    def setUp(self):
        '''
        test that will run before every test
        '''
        self.new_source = News(1, 'news','article source','bbc.com', 'business')

    def test_init(self):
        '''
        test if object is instantiated correctly
        '''
        self.assertEqual(self.new_article.id, 1)
        self.assertEqual(self.new_article.description, "news")
        self.assertEqual(self.new_article.name, "article source")
         self.assertEqual(self.new_article.url, "bbc.com")
        self.assertEqual(self.new_article.category, "business")
   