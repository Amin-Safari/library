from extensions import db
from datetime import datetime

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    loan_date = db.Column(db.DateTime, default=datetime.utcnow)
    return_date = db.Column(db.DateTime)
    is_returned = db.Column(db.Boolean, default=False)
    
    book = db.relationship('Book', backref=db.backref('loans', lazy=True))
    member = db.relationship('Member', backref=db.backref('loans', lazy=True))
    
    def to_dict(self):
        return {
            'id': self.id,
            'book_id': self.book_id,
            'member_id': self.member_id,
            'loan_date': self.loan_date,
            'return_date': self.return_date,
            'is_returned': self.is_returned
        }
    
    def __repr__(self):
        return f'<Loan {self.book.title} to {self.member.name}>' 