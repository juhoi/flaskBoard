from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    return 'Board index'


@bp.route('/hello')
def hello_board():
    return 'Hello, board~!'
