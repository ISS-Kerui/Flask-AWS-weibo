# -*- coding: utf-8 -*-
from flask import Blueprint

application = Blueprint('auth', __name__)

from . import views
