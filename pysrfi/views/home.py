from pyramid.view import view_config
from pyramid.events import subscriber, ApplicationCreated
from couchdbkit import *

from ..factory import Site
from ..models import Literal, Srfi

@view_config(context=Site, renderer='pages/home.mako', permission="view")
def home(request):
    return {
        "ctx": request.context
    }
