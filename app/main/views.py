from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news,get_article
from ..models import Article,News

@main.route('/')
def index():
    '''
    view root function that return the index page
    '''
    news = get_article('business')
    title = 'Welcome to The news highlight'
       
    return render_template('index.html',title = title, article=news)



# @main.route('/general')
# def general():
# 	'''
# 	View root page function that returns the index page and its data
# 	'''

# 	general = get_news('general')
# 	title = 'general-news Page - Get The latest News Online'
# 	return render_template('general.html',title = title,general=genera)

@main.route('/sports')
def sport():
	'''
	View root page function that returns the index page and its data
	'''

	sport = get_article('sports')
	title = 'general-news Page - Get The latest News Online'
	return render_template('sports.html',title = title,article=sport)

@main.route('/technology')
def tech():
	'''
	View root page function that returns the index page and its data
	'''

	technology = get_article('technology')
	title = 'general-news Page - Get The latest News Online'
	return render_template('technology.html',title = title,article=technology)

@main.route('/business')
def business():
	'''
	View root page function that returns the index page and its data
	'''

	business = get_article('business')
	title = 'general-news Page - Get The latest News Online'
	return render_template('business.html',title = title,article=business)

@main.route('/entertainment')
def entertainment():
	'''
	View root page function that returns the index page and its data
	'''
	# Getting popular news
	entertainment = get_article('entertainment')
	title = 'general-news Page - Get The latest News Online'
	return render_template('entertainment.html',title = title,article=entertainment)
