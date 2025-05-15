from flask import request, render_template, redirect, url_for, flash
from extensions import db
from models.loan import Loan
from models.book import Book
from models.member import Member
from controllers.history_controller import HistoryController
from controllers.blacklist_controller import BlacklistController
from datetime import datetime, timedelta

class LoanController:
    @staticmethod
    def index():
        active_loans = Loan.query.filter_by(is_returned=False).all()
        return render_template('loans.html', loans=active_loans)
    
    @staticmethod
    def create_loan(book_id):
        book = Book.query.get_or_404(book_id)
        
        if not book.is_available:
            flash('این کتاب در دسترس نیست')
            return redirect(url_for('books.index'))
        
        if request.method == 'POST':
            try:
                member_id = request.form['member_id']
                
                # بررسی لیست سیاه
                if BlacklistController.is_member_blacklisted(member_id):
                    flash('این عضو در لیست سیاه قرار دارد و مجاز به امانت گرفتن کتاب نیست')
                    members = Member.query.all()
                    return render_template('loan_book.html', book=book, members=members)
                
                loan = Loan(
                    book_id=book_id,
                    member_id=member_id,
                    return_date=datetime.utcnow() + timedelta(days=14)
                )
                book.is_available = False
                db.session.add(loan)
                db.session.commit()
                
                # ثبت در تاریخچه
                HistoryController.add_record(book_id, member_id, 'loan')
                
                flash('کتاب امانت داده شد')
                return redirect(url_for('books.index'))
            except Exception as e:
                flash('خطا در امانت دادن کتاب')
        
        members = Member.query.all()
        return render_template('loan_book.html', book=book, members=members)
    
    @staticmethod
    def return_book(loan_id):
        try:
            loan = Loan.query.get_or_404(loan_id)
            loan.is_returned = True
            loan.book.is_available = True
            db.session.commit()
            
            # ثبت در تاریخچه
            HistoryController.add_record(loan.book_id, loan.member_id, 'return')
            
            flash('کتاب برگردانده شد')
        except Exception as e:
            flash('خطا در برگرداندن کتاب')
        return redirect(url_for('loans.index')) 