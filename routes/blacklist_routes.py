from flask import Blueprint
from controllers.blacklist_controller import BlacklistController

blacklist_bp = Blueprint('blacklist', __name__)

@blacklist_bp.route('/')
def index():
    return BlacklistController.index()

@blacklist_bp.route('/add', methods=['GET', 'POST'])
def add():
    return BlacklistController.add()

@blacklist_bp.route('/remove/<int:blacklist_id>')
def remove(blacklist_id):
    return BlacklistController.remove(blacklist_id) 