#!/usr/bin/python3
"""importBlueprint"""

from flask import Blueprint
"""create a variable with an instance Blueprint"""
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.review import Review

import api.v1.views.index
import api.v1.views.states
import api.v1.views.cities
from api.v1.views.amenities
from api.v1.views.users
from api.v1.views.places
from api.v1.views.places_reviews
