from extensions import db
from datetime import datetime

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    action = db.Column(db.String(50), nullable=False)  # 'loan' یا 'return'
    date = db.Column(db.DateTime, default=datetime.utcnow)
    details = db.Column(db.Text, nullable=True)
    
    book = db.relationship('Book')
    member = db.relationship('Member')
    
    def __repr__(self):
        return f'<History {self.action} {self.book.title} - {self.member.name}>' 