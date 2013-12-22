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

class Resource(dict):
    def __init__(self, request, doc):
        self.request = request
        if doc.get('$ref'):
            doc = request.db[doc.get('$ref')]

        dict.__init__(self, doc) 

    def __getitem__(self, key):
        if self.get('doc_type') == 'view':
            view_name = self.get('view')
            design_name = self.get('design')

            return get_resource_by_view(self.request, key, "%s/%s" % (design_name, view_name))

        return Resource(self.request, self.get(key))

class Site(object):
    def __init__(self, request):
        self.request = request
        self.__parent__ = None
        self.__name__ = None
        self.current = request.db['root']

    def __getitem__(self, key):
        resource = Resource(self.request, self.current[key])
        
        if resource:
            resource.__name__ = key
            resource.__parent__ = self

            return resource

        raise KeyError

def get_root(request):
    return Site(request)
