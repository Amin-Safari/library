from flask import request, render_template, redirect, url_for, flash
from extensions import db
from models.book import Book

class BookController:
    @staticmethod
    def index():
        search = request.args.get('search', '')
        if search:
            books = Book.query.filter(
                Book.title.contains(search) | 
                Book.author.contains(search) |
                Book.category.contains(search)
            ).all()
        else:
            books = Book.query.all()
        return render_template('books.html', books=books)
    
    @staticmethod
    def create():
        if request.method == 'POST':
            try:
                book = Book(
                    title=request.form['title'],
                    author=request.form['author'],
                    year=int(request.form['year']),
                    category=request.form['category']
                )
                db.session.add(book)
                db.session.commit()
                flash('کتاب با موفقیت اضافه شد')
                return redirect(url_for('books.index'))
            except Exception as e:
                flash('خطا در اضافه کردن کتاب')
                return render_template('add_book.html')
        return render_template('add_book.html')
    
    @staticmethod
    def get_all():
        return Book.query.all()
    
    @staticmethod
    def get_by_id(book_id):
        return Book.query.get_or_404(book_id) 