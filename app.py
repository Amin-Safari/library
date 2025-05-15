# app.py
from flask import Flask
from dotenv import load_dotenv
import os
from extensions import db

def create_app():
    load_dotenv()
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///library.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    # Import blueprints
    from routes.main_routes import main_bp
    from routes.book_routes import book_bp
    from routes.member_routes import member_bp
    from routes.loan_routes import loan_bp
    from routes.history_routes import history_bp
    from routes.blacklist_routes import blacklist_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(book_bp, url_prefix='/books')
    app.register_blueprint(member_bp, url_prefix='/members')
    app.register_blueprint(loan_bp, url_prefix='/loans')
    app.register_blueprint(history_bp, url_prefix='/history')
    app.register_blueprint(blacklist_bp, url_prefix='/blacklist')
    
    return app

app = create_app()

@app.before_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)