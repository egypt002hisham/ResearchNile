from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/Research')
def Research():
    return render_template('Research.html')

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
    app.run(host='0.0.0.0', port=80 ,debug=True)
