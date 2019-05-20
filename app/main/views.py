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



@main.route('/general')
def general():
	'''
	View root page function that returns the index page and its data
	'''

	general = get_news('general')
	title = 'general-news Page - Get The latest News Online'
	return render_template('general.html',title = title,general=genera)

@main.route('/sports')
def sport():
	'''
	View root page function that returns the index page and its data
	'''

	sports = get_news('sports')
	title = 'general-news Page - Get The latest News Online'
	return render_template('sports.html',title = title,sports=sports)

@main.route('/technology')
def tech():
	'''
	View root page function that returns the index page and its data
	'''

	general_news = get_news('technology')
	title = 'general-news Page - Get The latest News Online'
	return render_template('technology.html',title = title,technology=general_news)

@main.route('/business')
def business():
	'''
	View root page function that returns the index page and its data
	'''

	general_news = get_news('business')
	title = 'general-news Page - Get The latest News Online'
	return render_template('businessNews.html',title = title,businessNews=general_news)

@main.route('/entertainment')
def entertainment():
	'''
	View root page function that returns the index page and its data
	'''
	# Getting popular news
	general_news = get_news('entertainment')
	title = 'general-news Page - Get The latest News Online'
	return render_template('entertainmentNews.html',title = title,entertainment=general_news)
