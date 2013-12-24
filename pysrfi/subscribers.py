from pyramid.view import view_config
from pyramid.events import subscriber, ApplicationCreated
from couchdbkit import *

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
