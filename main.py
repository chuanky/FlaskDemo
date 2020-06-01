from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '768e9bbafaff31383498b62688f3e2c7'

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

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('hello'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
