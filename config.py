class Config:
    '''
    General configurations parent class
    '''
    ARTICLE_BASE_URL = 'https://newsapi.org/v2/everything?domains={}&language=en&apiKey={}'
    #SOURCE_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'

class DevConfig(Config):
    '''
    development configurations class that inherits from Config parent class
    '''
    DEBUG = True
class ProdConfig(Config):
    '''
    Production configurtions that inherits from Config parent 
    '''
    pass

config_options ={
    'development': DevConfig,
    'production': ProdConfig
}