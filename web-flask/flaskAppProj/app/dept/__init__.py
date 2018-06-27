from flask import Blueprint

dept = Blueprint('dept', __name__,)

from app.dept import views