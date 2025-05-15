from flask import Blueprint
from controllers.history_controller import HistoryController

history_bp = Blueprint('history', __name__)

@history_bp.route('/')
def index():
    return HistoryController.index() 