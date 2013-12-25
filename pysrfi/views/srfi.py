from pyramid.view import view_config
from pyramid.events import subscriber, ApplicationCreated
from couchdbkit import *

import time
from datetime import datetime
from markdown import markdown as _m, Markdown
from logging import getLogger

from ..factory import Site
from ..models import Page, Literal, Srfi

logger = getLogger(__file__)

exts = ['def_list', 'tables', 'fenced_code', 'toc', 'abbr', 'footnotes']

def markdown(text):
    return _m(text, extensions=exts)

def mark2(text):
    md = Markdown(extensions=exts)
    text = md.convert(text)
    return (text, md.toc)

def process_content(obj):
    obj = obj.copy()

    obj["content"], obj["toc"] = map(Literal,
                                     mark2(obj.get("content")))

    obj["created"], obj["updated"] = map(int_to_datetime,
                                         [obj.get("created"),
                                          obj.get("updated")])

    return obj

def int_to_datetime(timestamp):
    return datetime.fromtimestamp(timestamp / 1e3)

def datetime_to_int(thetime):
    return time.mktime(thetime.timetuple()) * 1e3

def update_doc(document, params):
    now = datetime.now()

    doc = document.copy()

    doc.update({
        "title": params.get("title"),
        "author": params.get("author"),
        "content": params.get("content"),
        "status": params.get("status"),
        "updated": datetime_to_int(now),
        "previous": params.get("_id"),
        "version": document.get("version") + 1,
    })

    return doc

@view_config(name="revisions", doc_type='Srfi', renderer='srfi/versions.mako')
def versions(request):

    versions = []
    for i in request.context.__context:
        doc = i.get('doc')
        versions.append((doc.get('date'), doc.get('version')))

    doc = process_content(request.context)

    return {
        'versions': versions,
        'version': request.context.get('version'),
        "ctx": doc
    }


@view_config(name="save", doc_type='Srfi', renderer='srfi/show.mako')
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

    page = Srfi(doc)

    page.version = page.version + 1 if page.version else 1
    page.save()

    doc = process_content(page.to_json())
    
    return {
        "ctx": doc
    }

@view_config(name="revision", doc_type='Srfi', renderer='srfi/show.mako')
def version(request):
    doc = None
    version = request.subpath[0]

    for i in request.context.__context:
        if i.get('doc').get('version') == int(version):
            doc = process_content(i.get('doc'))

    if not doc:
        raise KeyError

    return {
        "ctx": doc
    }

@view_config(name="edit", doc_type='Srfi', renderer='srfi/show.mako', request_method="POST")
def edit_post(request):
    doc = update_doc(request.context, request.params)

    page = Srfi(doc)
    page.save()

    doc = process_content(page.to_json())

    return {
        "ctx": doc
    }

@view_config(name="edit", doc_type='Srfi', renderer='srfi/edit.mako')
def edit(request):

    doc = request.context

    return {
        "ctx": doc
    }

@view_config(doc_type='Srfi', renderer='srfi/show.mako')
def show(request):

    doc = process_content(request.context)

    return {
        "ctx": doc
    }
