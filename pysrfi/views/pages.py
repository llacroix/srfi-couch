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

    response = request.response
    headers = remember(request, email)
    response.headerlist.extend(headers)
    return HTTPFound(location="/", headers=headers)

    return {
        "ctx": request.context.profile
    }

@view_config(route_name="logout", renderer="json")
def logout(request):
    response = request.response
    headers = forget(request)
    response.headerlist.extend(headers)

    return {
        "lgout": "ok"
    } 

@view_config(doc_type="Page", renderer='pages/page.mako', permission="view")
def show_page(request):

    return {
        "ctx": request.context
    }
