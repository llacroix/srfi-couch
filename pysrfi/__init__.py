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
        if context:
            return context.get('doc_type', None) == self.val
        else:
            return False

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=get_root, settings=settings)

    config.registry.db = Server(uri=settings['couchdb.uri'])

    def add_couchdb(request):
        db = config.registry.db.get_or_create_db(settings['couchdb.db'])
        return db

    config.add_request_method(add_couchdb, 'db', reify=True)
    config.add_view_predicate('doc_type', DocumentType)

    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    #config.add_route('home', '/')
    config.scan()

    return config.make_wsgi_app()
