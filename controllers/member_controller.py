from flask import request, render_template, redirect, url_for, flash
from extensions import db
from models.member import Member

class MemberController:
    @staticmethod
    def index():
        members = Member.query.all()
        return render_template('members.html', members=members)
    
    @staticmethod
    def create():
        if request.method == 'POST':
            try:
                member = Member(
                    name=request.form['name'],
                    email=request.form['email'],
                    phone=request.form.get('phone', '')
                )
                db.session.add(member)
                db.session.commit()
                flash('عضو با موفقیت اضافه شد')
                return redirect(url_for('members.index'))
            except Exception as e:
                flash('خطا در اضافه کردن عضو')
                return render_template('add_member.html')
        return render_template('add_member.html')
    
    @staticmethod
    def get_all():
        return Member.query.all()
    
    @staticmethod
    def get_by_id(member_id):
        return Member.query.get_or_404(member_id) 