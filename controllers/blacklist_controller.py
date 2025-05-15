from flask import render_template, redirect, url_for, request, flash
from models.blacklist import Blacklist
from models.member import Member
from extensions import db
from datetime import datetime

class BlacklistController:
    @staticmethod
    def index():
        # نمایش لیست سیاه
        blacklist = Blacklist.query.filter_by(is_active=True).all()
        return render_template('blacklist.html', blacklist=blacklist)
    
    @staticmethod
    def add():
        # افزودن عضو به لیست سیاه
        if request.method == 'POST':
            member_id = request.form['member_id']
            reason = request.form['reason']
            end_date_str = request.form.get('end_date')
            
            # بررسی آیا عضو قبلاً در لیست سیاه است
            existing = Blacklist.query.filter_by(member_id=member_id, is_active=True).first()
            if existing:
                flash('این عضو در حال حاضر در لیست سیاه قرار دارد')
                return redirect(url_for('blacklist.index'))
            
            end_date = None
            if end_date_str:
                try:
                    # تبدیل تاریخ از متن به شی datetime
                    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
                except ValueError:
                    flash('فرمت تاریخ نامعتبر است')
                    members = Member.query.all()
                    return render_template('add_to_blacklist.html', members=members)
            
            blacklist = Blacklist(
                member_id=member_id,
                reason=reason,
                end_date=end_date
            )
            
            db.session.add(blacklist)
            db.session.commit()
            flash('عضو با موفقیت به لیست سیاه اضافه شد')
            return redirect(url_for('blacklist.index'))
        
        members = Member.query.all()
        return render_template('add_to_blacklist.html', members=members)
    
    @staticmethod
    def remove(blacklist_id):
        # حذف عضو از لیست سیاه
        blacklist = Blacklist.query.get_or_404(blacklist_id)
        blacklist.is_active = False
        db.session.commit()
        flash('عضو از لیست سیاه حذف شد')
        return redirect(url_for('blacklist.index'))
    
    @staticmethod
    def is_member_blacklisted(member_id):
        """بررسی آیا عضو در لیست سیاه است یا خیر"""
        now = datetime.utcnow()
        
        # عضو در لیست سیاه است اگر:
        # 1. رکورد فعال داشته باشد
        # 2. تاریخ پایان نامشخص باشد یا هنوز نرسیده باشد
        blacklist = Blacklist.query.filter_by(member_id=member_id, is_active=True).first()
        
        if not blacklist:
            return False
        
        # اگر تاریخ پایان ندارد (دائمی است) یا هنوز به تاریخ پایان نرسیده‌ایم
        if not blacklist.end_date or blacklist.end_date > now:
            return True
        
        # اگر تاریخ پایان گذشته است، رکورد را غیرفعال کنیم
        blacklist.is_active = False
        db.session.commit()
        return False 