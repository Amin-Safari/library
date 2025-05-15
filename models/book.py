from extensions import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    is_available = db.Column(db.Boolean, default=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'category': self.category,
            'is_available': self.is_available
        }
    
    def __repr__(self):
        return f'<Book {self.title}>' 