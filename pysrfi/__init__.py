from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.config import Configurator
from couchdbkit import *
from factory import get_root

class DocumentType(object):
    def __init__(self, val, config):
        self.val = val

    def text(self):
        return 'content_type = %s' % (self.val,)

    phash = text

    def __call__(self, context, request):
        if context and "get" in dir(context):
            return context.get('doc_type', None) == self.val
        else:
            return False

def groupfinder(userid, request):
    user = request.db.get(userid)
    if user:
        return ['g:%s' % g for g in user.get("groups", [])]

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    authn_policy = AuthTktAuthenticationPolicy(
        "othersecret",
        callback=groupfinder,
    )
    authz_policy = ACLAuthorizationPolicy()

    my_session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')

    config = Configurator(root_factory=get_root,
                          settings=settings,
                          authentication_policy=authn_policy,
                          authorization_policy=authz_policy,
                          session_factory=my_session_factory)

    config.registry.db = Server(uri=settings['couchdb.uri'])

    def add_couchdb(request):
        db = config.registry.db.get_or_create_db(settings['couchdb.db'])
        return db

    config.add_request_method(add_couchdb, 'db', reify=True)
    config.add_view_predicate('doc_type', DocumentType)

    config.include('pyramid_chameleon')

    config.add_static_view('static', 'static', cache_max_age=3600)

    config.include('velruse.providers.google_hybrid')
    config.add_route("logout", "/logout")
    #config.add_openid_login()
    config.add_google_hybrid_login()

    config.scan()

    return config.make_wsgi_app()
