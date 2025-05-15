from flask import Blueprint
from controllers.loan_controller import LoanController

loan_bp = Blueprint('loans', __name__)

@loan_bp.route('/')
def index():
    return LoanController.index()

@loan_bp.route('/book/<int:book_id>', methods=['GET', 'POST'])
def loan_book(book_id):
    return LoanController.create_loan(book_id)

@loan_bp.route('/return/<int:loan_id>')
def return_book(loan_id):
    return LoanController.return_book(loan_id) 