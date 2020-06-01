from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'chuanqi',
        'title': 'title_chuanqi',
        'content': 'content_chuanqi'
    },
    {
        'author': 'mige',
        'title': 'title_mige',
        'content': 'content_mige'
    }
]

@app.route('/')
def hello():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
