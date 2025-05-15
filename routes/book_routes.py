from flask import Blueprint
from controllers.book_controller import BookController

book_bp = Blueprint('books', __name__)

@book_bp.route('/')
def index():
    return BookController.index()

@book_bp.route('/add', methods=['GET', 'POST'])
def add():
    return BookController.create() 