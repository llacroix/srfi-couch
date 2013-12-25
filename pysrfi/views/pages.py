from pyramid.view import view_config
from pyramid.events import subscriber, ApplicationCreated
from couchdbkit import *

from ..factory import Site
from ..models import Literal, Srfi

@view_config(doc_type="Page", renderer='pages/page.mako')
def show_page(request):
    return {
        "ctx": request.context
    }
