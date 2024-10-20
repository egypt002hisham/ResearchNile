from flask import Flask, jsonify, redirect, render_template, request, session, url_for, flash 
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from datetime import timedelta
import os
import myClass  
import markdown  # استيراد المكتبة

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'a_random_secret_key')
app.config['SESSION_TYPE'] = 'filesystem'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB
app.config['SESSION_COOKIE_HTTPONLY'] = True  # Prevents JavaScript from accessing session cookies
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # Helps protect against CSRF attacks
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=365)

@app.route('/')
def index():
    articles = myClass.LatestDirectory.process_latest_directory()  # استدعاء 
    return render_template('Research.html', articles=articles)  # تمرير المقالات إلى القالب

@app.route('/Research')
def Research():
    articles = myClass.LatestDirectory.process_latest_directory()  # استدعاء 
    return render_template('Research.html', articles=articles)  # تمرير المقالات إلى القالب



@app.route('/article/<article_id>')
def article(article_id):
    # استدعاء الدالة لمعالجة المجلدات وجلب المقالات
    articles = myClass.LatestDirectory.process_latest_directory()

    # البحث عن المقال باستخدام article_id
    article_data = next((article for article in articles if article['id'] == article_id), None)
    
    if article_data is None:
        # إذا لم يتم العثور على المقال
        return "Article not found", 404

    # تحويل محتوى المقال من Markdown إلى HTML
    article_html = markdown.markdown(article_data['article'])
    
    # تمرير البيانات إلى القالب لعرضها في المتصفح
    return render_template('article.html', article=article_data, article_html=article_html)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')  # Route for the Contact page
def contact():
    return render_template('contact.html')

@app.route('/home')  
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
