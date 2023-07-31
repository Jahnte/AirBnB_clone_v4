#!/usr/bin/python3
"""Blueprint for API"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

"""import views module wont be checked for PEP8"""
import api.v1.views.index
