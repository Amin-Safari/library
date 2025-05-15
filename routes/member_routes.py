# routes/member_routes.py
from flask import Blueprint, render_template
from extensions import db
from models.member import Member
from controllers.member_controller import MemberController

member_bp = Blueprint('members', __name__)

@member_bp.route('/')
def index():
    return MemberController.index()

@member_bp.route('/add', methods=['GET', 'POST'])
def add():
    return MemberController.create() 