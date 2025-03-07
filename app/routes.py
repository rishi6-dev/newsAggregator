from flask import render_template, request, redirect, url_for
from app import app
from app.news import category  # Import the category function from news.py

@app.route('/')
def index():
    categories = ["Sports", "Tech", "India", "World", "Markets"]  
    return render_template('index.html', categories=categories)


@app.route('/category/<category_name>', methods=['GET', 'POST'])
def category_page(category_name):
    news_list = category(category_name)
    
    if not news_list:
        return redirect(url_for('index'))  
    
    return render_template('category.html', category=category_name, news_list=news_list)