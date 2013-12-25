from models import Page

def get_resource_by_view(request, key, view):
    pages = list(request.db.view(view,
                                startkey=[key],
                                endkey=[key, {}],
                                reduce=False,
                                include_docs=True))
    if len(pages) > 0:
        ret = Resource(request, pages[0].get('doc'))
        ret.__context = pages
        return ret

def get_sub_resource(self, request, key):
    if self.get('doc_type') == 'view':
        view_name = self.get('view')
        design_name = self.get('design')

        return get_resource_by_view(request, key, "%s/%s" % (design_name, view_name))

    if not key in self.keys():
        raise KeyError

    doc = self.get(key)

    if doc.get('$ref'):
        return Resource(request, request.db[doc.get('$ref')])

    if isinstance(doc, dict):
        return Resource(request, doc)

    return doc


class Resource(dict):
    def __init__(self, request, doc):
        self.request = request
        dict.__init__(self, doc) 

    def __getitem__(self, key):
        child = get_sub_resource(self, self.request, key)

        if child:
            child.__name__ = key
            child.__parent__ = self

            if child.get('@acl'):
                child.__acl__ = child.get('@acl')

            return child
        else:
            raise KeyError

    def __repr__(self):
        return self.keys().__str__()

    def url(self, *args):
        return self.request.resource_url(self, *args)

from pyramid.security import Allow
from pyramid.security import Everyone

class Site(object):
    def __init__(self, request):
        self.request = request
        self.__parent__ = None
        self.__name__ = None
        self.__acl__ = [
            (Allow, Everyone, 'view'),
            (Allow, 'g:editors', 'edit')
        ]
        self.current = request.db['root']

    def __getitem__(self, key):
        resource = get_sub_resource(self.current, self.request, key)
        
        if resource:
            resource.__name__ = key
            resource.__parent__ = self

            if resource.get('@acl'):
                resource.__acl__ = resource.get('@acl')


            return resource

        raise KeyError

def get_root(request):
    return Site(request)
