# from crypt import methods
from phim.models import User, Movie
from flask import render_template, url_for, flash, redirect, request
from phim.forms import RegistrationForm, LoginForm, MovieForm, UpdateAccountForm
from phim import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
import os
from PIL import Image
import secrets

def save_picture(form_picture, path):
    picture_fn = form_picture.filename
    picture_path = os.path.join(app.root_path, path, picture_fn)
    i = Image.open(form_picture)
    i.save(picture_path)
    return picture_fn

@app.route("/")
def home():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful! Please check email or password', 'danger')
    return render_template('login.html', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # picture_file = save_picture(form.image.data, path='static/prof_pics')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register Page', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if current_user.username != 'admin':
        flash('You are not admin!', 'danger')
        return redirect(url_for('home'))
    form = MovieForm()
    if form.validate_on_submit():
        picture_file = save_picture(form.image.data, path='static/movie_pics')
        movie = Movie(movie_eng=form.movie_eng.data, movie_vn=form.movie_vn.data, year=form.year.data, imdb=form.imdb.data, summary=form.summary.data, author=form.author.data, nation=form.nation.data, image=picture_file, link=form.link.data, tl=form.tl.data)
        db.session.add(movie)
        db.session.commit()
        flash(f'Movie has been uploaded!', 'success')
        return redirect(url_for('home'))
    return render_template('upload.html', form=form)

@app.route("/movie/<int:movie_id>")
def movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    return render_template('xemphim.html', movie=movie)

@app.route('/private', methods=['GET', 'POST'])
@login_required
def private():
    image_file = url_for('static', filename='prof_pics/' + current_user.image)
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data, "static/prof_pics")
            current_user.image = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('private'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    return render_template('private-page.html', image_file=image_file, form=form)

@app.route('/watch/<int:movie_id>')
def watch_film(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    return render_template('watch-film.html', movie=movie)

@app.route('/xemphim')
@login_required
def xemphim():
    return render_template('xemphim.html')

@app.route('/phimle', methods=['GET', 'POST'])
def phimle():
    movies = Movie.query.filter_by(tl='PL').all()
    return render_template('loc_phim.html', movies=movies, theloai='Phim Le')

@app.route('/phimbo', methods=['GET', 'POST'])
def phimbo():
    movies = Movie.query.filter_by(tl='PB').all()
    return render_template('loc_phim.html', movies=movies, theloai='Phim Bo')

@app.route('/phimhot', methods=['GET', 'POST'])
def phimhot():
    movies = Movie.query.order_by(Movie.imdb.desc()).all()
    return render_template('loc_phim.html', movies=movies, theloai='Phim Hot')

@app.route('/phimmoi', methods=['GET', 'POST'])
def phimmoi():
    movies = Movie.query.order_by(Movie.year.desc()).all()
    return render_template('loc_phim.html', movies=movies, theloai='Phim Moi')


