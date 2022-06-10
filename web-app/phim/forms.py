from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, FloatField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from phim.models import User, Movie
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    # image = FileField('Image', validators=[FileAllowed(['jpg', 'png']), FileRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one!')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one!')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class MovieForm(FlaskForm):
    movie_eng = StringField('Movie name by English', validators=[DataRequired()])
    movie_vn = StringField('Movie name by Vietnamese', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
    imdb = FloatField('IMDB', validators=[DataRequired()])
    summary = TextAreaField('Summary', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    nation = StringField('Nation', validators=[DataRequired()])
    image = FileField('Image', validators=[FileAllowed(['jpg', 'png']), FileRequired()])
    link = StringField('Embedded Link', validators=[DataRequired()])
    tl = SelectField('The loai', choices=[('PL', 'Phim le'), ('PB', 'Phim bo')])

    submit = SubmitField('Upload')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])

    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')
