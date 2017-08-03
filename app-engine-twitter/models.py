from google.appengine.ext import ndb


class Response2(ndb.Model):
    responser = ndb.StringProperty(required = True)
