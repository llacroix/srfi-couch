
@view_config(context=Site, renderer='home.mako')
def home(request):
    return {
        'project': 'pyramid_couchdb_example'
    }
