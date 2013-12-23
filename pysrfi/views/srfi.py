from pyramid.view import view_config
from pyramid.events import subscriber, ApplicationCreated
from couchdbkit import *
import datetime
from datetime import datetime
from markdown import markdown as _m, Markdown
from logging import getLogger

from ..factory import Site
from ..models import Page, Literal, Srfi

logger = getLogger(__file__)

exts = ['def_list', 'tables', 'fenced_code', 'toc', 'abbr', 'footnotes']

def markdown(text):
    return _m(text, extensions=exts)

@subscriber(ApplicationCreated)
def application_created_subscriber(event):
    registry = event.app.registry
    db = registry.db.get_or_create_db(registry.settings['couchdb.db'])

    Document.set_db(db)

    pages_view_exists = db.doc_exist('_design/lists')

    if pages_view_exists == False:
        design_doc = {
            '_id': '_design/lists',
            'language': 'javascript',
            'views': {
                'pages': {
                    'map': '''
                        function(doc) {
                            if (doc.doc_type === 'Page' || doc.doc_type === 'Srfi') {
                                emit([doc.page,
                                      doc.version ? -doc.version : 0],
                                     null)
                            }
                        }
                    '''
                }
            }
        }

        db.save_doc(design_doc)

@view_config(context=Site, renderer='home.mako')
def home(request):
    return {
        'project': 'pyramid_couchdb_example'
    }

@view_config(name="versions", doc_type='Srfi', renderer='versions.mako')
def versions(request):
    versions = []
    for i in request.context.__context:
        doc = i.get('doc')
        versions.append((doc.get('date'), doc.get('version')))

    return {
        'project': 'asasd',
        'versions': versions,
        'version': request.context.get('version'),
        'title': request.context.get('title'),
        'author': request.context.get('author'),
    }

@view_config(name="version", doc_type='Srfi', renderer='srfi.mako')
def version(request):
    doc = {}
    version = request.subpath[0]

    for i in request.context.__context:
        if i.get('doc').get('version') == int(version):
            doc = i.get('doc')

    return {
        'project': 'pyramid_couchdb_example',
        'info': request.db.info(),
        'title': doc.get('title'),
        'author': doc.get('author'),
        'content': markdown(doc.get('content') or ''),
        'date': doc.get('date'),
        'version': doc.get('version', 0)
    }

@view_config(name="save", doc_type='Srfi', renderer='srfi.mako')
def save(request):
    doc = request.context

    doc['date'] = datetime.now()
    doc['previous'] = doc['_id']
    doc['content'] = doc['content'].replace('<code>', '`').replace('</code>', '`')
    doc['content'] = doc['content'].replace('<var>', '`').replace('</var>', '`')
    doc['content'] = doc['content'].replace('<p>', '').replace('</p>', '')
    doc['content'] = doc['content'].replace('<em>', '*').replace('</em>', '*')
    doc['content'] = doc['content'].replace('&gt;', '>').replace('&lt;', '<')
    doc['content'] = doc['content'].replace(';``', '; ').replace('&nbsp;', '')
    doc['content'] = doc['content'].replace('``', '').replace('<code class=proc-def>', '')
    doc['content'] = doc['content'].replace('<dd class=proc-def>\n ', ':')

    del doc['_id']
    del doc['_rev']

    page = Page(doc)

    page.version = page.version + 1 if page.version else 1
    page.save()

    md = Markdown(extensions=exts)
    text = md.convert(page.content)
    
    return {
        'project': 'pyramid_couchdb_example',
        'info': request.db.info(),
        'title': page.title,
        'author': page.author,
        'content': text,
        'toc': md.toc,
        'date': page.date,
        'version': page.version
    }

@view_config(name="edit", doc_type='Srfi', renderer='srfi.mako', request_method="POST")
def edit_post(request):
    doc = request.context
    params = request.params

    del doc['_id']
    del doc['_rev']

    page = Srfi(doc)
    page.title = params.get('title')
    page.author = params.get('author')
    page.content = params.get('content')
    page.status = params.get('status')
    page.previous = params.get('_id')
    page.version += 1

    page.save()

    doc = page.to_json()

    md = Markdown(extensions=exts)
    text = md.convert(doc.get('content'))

    return {
        'project': 'pyramid_couchdb_example',
        'info': request.db.info(),
        'title': doc.get('title'),
        'author': doc.get('author'),
        'content': text,
        'toc': md.toc,
        'date': doc.get('date'),
        'version': doc.get('version', 0)
    }

@view_config(name="edit", doc_type='Srfi', renderer='edit.mako')
def edit(request):
    return request.context

@view_config(doc_type='Srfi', renderer='srfi.mako')
def show(request):

    doc = request.context

    md = Markdown(extensions=exts)
    text = md.convert(doc.get('content'))

    return {
        'project': 'pyramid_couchdb_example',
        'info': request.db.info(),
        'title': doc.get('title'),
        'author': doc.get('author'),
        'content': text,
        'toc': md.toc,
        'date': doc.get('date'),
        'version': doc.get('version', 0)
    }
