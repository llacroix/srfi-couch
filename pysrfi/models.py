from couchdbkit import *

class Srfi(Document):
    author = StringProperty()
    title = StringProperty()
    content = StringProperty()
    date = DateTimeProperty()
    version = IntegerProperty()

class Page(Document):
    author = StringProperty()
    title = StringProperty()
    content = StringProperty()
    date = DateTimeProperty()
    version = IntegerProperty()

class Literal(object):
    def __init__(self, content):
        self.content = content

    def __html__(self):
        return self.content
