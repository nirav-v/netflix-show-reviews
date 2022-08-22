from flask import Blueprint, render_template, session, redirect
from app.models import Post, Movie
from app.db import get_db

bp = Blueprint('home', __name__, url_prefix='/')


@bp.route('/')
def index():
    # get all posts
    db = get_db()

    movies = db.query(Movie).order_by(Movie.title)
    return render_template(
        'movies.html',
        movies=movies
    )


@bp.route('/login')
def login():
    # not logged in yet
    if session.get('loggedIn') is None:
        return render_template('login.html')

    return redirect('/')


# @bp.route('/post/<id>')
# def single(id):
#     # get single post by id
#     db = get_db()
#     post = db.query(Post).filter(Post.id == id).one()

#     # render single post template
#     return render_template(
#         'single-post.html',
#         post=post,
#         loggedIn=session.get('loggedIn')
#     )

@bp.route('/movie/<id>')
def single(id):
    # get single movie by id
    db = get_db()
    movie = db.query(Movie).filter(Movie.id == id).one()

    # render single post template
    return render_template(
        'single-movie.html',
        movie=movie,
        loggedIn=session.get('loggedIn')
    )
