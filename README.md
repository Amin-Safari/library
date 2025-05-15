# سیستم مدیریت کتابخانه

یک برنامه کاربردی تحت وب برای مدیریت کتابخانه، با امکان ثبت و مدیریت کتاب‌ها، اعضا، امانت‌ها، تاریخچه و لیست سیاه.

## قابلیت‌ها

### مدیریت کتاب‌ها
- ثبت کتاب‌های جدید (عنوان، نویسنده، سال انتشار، دسته‌بندی)
- مشاهده لیست کتاب‌ها
- جستجو در کتاب‌ها براساس عنوان، نویسنده و دسته‌بندی

### مدیریت اعضا
- ثبت نام اعضای جدید
- مشاهده لیست اعضا

### مدیریت امانت‌ها
- ثبت امانت کتاب به اعضا
- بازگردانی کتاب‌های امانت داده شده
- مشاهده لیست امانت‌های فعال

### تاریخچه
- نمایش تاریخچه کامل امانت و بازگشت کتاب‌ها
- فیلتر کردن تاریخچه براساس کتاب یا عضو

### لیست سیاه
- افزودن اعضا به لیست سیاه با دلیل و مدت زمان مشخص
- ممانعت از امانت کتاب به افراد موجود در لیست سیاه
- امکان حذف افراد از لیست سیاه

## تکنولوژی‌های استفاده شده

### بک‌اند
- **Flask**: فریم‌ورک پایتون برای توسعه سریع وب اپلیکیشن
- **SQLAlchemy**: ORM (ابزار نگاشت شیء-رابطه‌ای) برای کار با پایگاه داده
- **Flask-SQLAlchemy**: ادغام SQLAlchemy با Flask
- **Python-dotenv**: برای مدیریت متغیرهای محیطی

### فرانت‌اند
- **HTML/CSS**: برای ساختار و استایل‌دهی صفحات
- **Bootstrap 5**: فریم‌ورک CSS برای طراحی واکنش‌گرا
- **Jinja2**: موتور قالب‌بندی برای تولید صفحات HTML پویا

### معماری
- **الگوی MVC (Model-View-Controller)**: برای سازماندهی کد و جداسازی لایه‌های مختلف برنامه
  - **Models**: تعریف ساختار پایگاه داده و ارتباط بین جداول
  - **Controllers**: منطق کسب‌وکار و پردازش درخواست‌ها
  - **Views (Templates)**: قالب‌های HTML برای نمایش به کاربر
- **Blueprints**: برای ماژولار کردن اپلیکیشن

### پایگاه داده
- **SQLite**: پایگاه داده سبک و بدون نیاز به سرور مجزا (قابل تغییر به MySQL یا PostgreSQL)

## نصب و راه‌اندازی

### پیش‌نیازها
- Python 3.8 یا بالاتر
- pip (مدیر بسته پایتون)

### مراحل نصب

1. **کلون کردن مخزن**
```bash
git clone <repository-url>
cd library-management-system
```

2. **ایجاد محیط مجازی**
```bash
python -m venv venv

# در ویندوز
venv\Scripts\activate

# در لینوکس و مک
source venv/bin/activate
```

3. **نصب وابستگی‌ها**
```bash
pip install -r requirements.txt
```

4. **تنظیم فایل .env**
```
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///library.db
FLASK_ENV=development
FLASK_DEBUG=1
```

5. **اجرای برنامه**
```bash
python app.py
```

برنامه روی آدرس `http://127.0.0.1:5000` قابل دسترسی خواهد بود.

## ساختار پروژه

```
library-management-system/
├── app.py                  # فایل اصلی برنامه
├── extensions.py           # تعریف ابجکت‌های مشترک (مثل db)
├── requirements.txt        # لیست وابستگی‌ها
├── .env                    # متغیرهای محیطی
├── models/                 # تعریف مدل‌های داده
│   ├── __init__.py
│   ├── book.py
│   ├── member.py
│   ├── loan.py
│   ├── history.py
│   └── blacklist.py
├── controllers/            # منطق کسب‌وکار
│   ├── __init__.py
│   ├── book_controller.py
│   ├── member_controller.py
│   ├── loan_controller.py
│   ├── history_controller.py
│   └── blacklist_controller.py
├── routes/                 # مسیریابی درخواست‌ها
│   ├── __init__.py
│   ├── main_routes.py
│   ├── book_routes.py
│   ├── member_routes.py
│   ├── loan_routes.py
│   ├── history_routes.py
│   └── blacklist_routes.py
└── templates/              # قالب‌های HTML
    ├── base.html           # قالب پایه
    ├── index.html
    ├── books.html
    ├── add_book.html
    ├── members.html
    ├── add_member.html
    ├── loans.html
    ├── loan_book.html
    ├── history.html
    ├── blacklist.html
    └── add_to_blacklist.html
```

## لایسنس

MIT 2024 Amin-Safari

---

**توسعه داده شده توسط امین صفری**
**تماس** : aminsafari1385@gmail.com
