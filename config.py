import os

class Config:
    '''
    General configurations parent class
    '''
    
    NEWS_BASE_URL ='https://newsapi.org/v2/sources?category={}&language=en&apiKey={}'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class DevConfig(Config):
    '''
    development configurations class that inherits from Config parent class
    '''
    DEBUG = True
class ProdConfig(Config):
    '''
    Production configurtions that inherits from Config parent 
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")#for heroku purposes

    

config_options ={
    'development': DevConfig,
    'production': ProdConfig
}