from pyramid.view import view_config
from pyramid.events import subscriber, ApplicationCreated
from pyramid.httpexceptions import HTTPFound

from couchdbkit import *

from pyramid.security import (
       remember,
       forget,
       authenticated_userid,
     )

from ..factory import Site
from ..models import Literal, Srfi

@view_config(route_name="velruse.google-callback", renderer="auth/logged.mako")
def openid_callback(request):
    email = request.context.profile['verifiedEmail']

    try:
        user = request.db[email]
    except ResourceNotFound as exc:
        user = {"email": email,
                "doc_type": "User",
                "name" : request.context.profile['displayName']
               }
        request.db[email] = user

    headers = remember(request, email)
    return HTTPFound(location="/", headers=headers)

    return {
        "ctx": request.context.profile
    }

@view_config(doc_type="Page", renderer='pages/page.mako')
def show_page(request):

    current = authenticated_userid(request)

    return {
        "current_user": current,
        "ctx": request.context
    }
