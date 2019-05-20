class News:

	'''
	News class that creates  News Objects
	'''
	def __init__(self, id, description,name, url, category):


		self.id = id
		self.name = name
		self.description = description
		self.url = url
		self.category = category



class Article:
    '''
    Article class that creates instances of article objects
    '''
    def __init__ (self, source, urlToImage, author,title,description,publishedAt,url):
        self.source = source
        self.urlToImage = urlToImage
        self.author = author
        self.title = title
        self.description = description
        self.publishedAt = publishedAt
        self.url = url
