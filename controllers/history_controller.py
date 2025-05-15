from flask import render_template, request
from models.history import History
from models.book import Book
from models.member import Member
from extensions import db

class HistoryController:
    @staticmethod
    def index():
        # امکان فیلتر کردن براساس عضو یا کتاب
        member_id = request.args.get('member_id')
        book_id = request.args.get('book_id')
        
        query = History.query
        
        if member_id:
            query = query.filter_by(member_id=member_id)
        
        if book_id:
            query = query.filter_by(book_id=book_id)
        
        history = query.order_by(History.date.desc()).all()
        members = Member.query.all()
        books = Book.query.all()
        
        return render_template('history.html', 
                               history=history, 
                               members=members, 
                               books=books,
                               selected_member=member_id,
                               selected_book=book_id)
    
    @staticmethod
    def add_record(book_id, member_id, action, details=None):
        """افزودن یک رکورد به تاریخچه"""
        history = History(
            book_id=book_id,
            member_id=member_id,
            action=action,
            details=details
        )
        db.session.add(history)
        db.session.commit() 