from extensions import db
from datetime import datetime

class Blacklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    reason = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=True)  # تاریخ پایان (اگر موقت باشد)
    is_active = db.Column(db.Boolean, default=True)
    
    member = db.relationship('Member', backref=db.backref('blacklist_records', lazy=True))
    
    def __repr__(self):
        return f'<Blacklist {self.member.name}>' 