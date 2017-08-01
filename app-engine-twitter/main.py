#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import jinja2
import os
import webapp2
import json
import io
import twitter





jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        my_template = jinja_environment.get_template('templates/twitter_shade.html')
        self.response.write(my_template.render())
# class TwitterHandler(webapp2.RequestHandler):
#     def get(self):
#         self.response.write(Query)
class AboutHandler(webapp2.RequestHandler):
    def get(self):
        my_template = jinja_environment.get_template('templates/about_page.html')
        self.response.write(my_template.render())
class TwitterHandler(webapp2.RequestHandler):
    def get(self):

        # XXX: Go to http://twitter.com/apps/new to create an app and get values
        # for these credentials that you'll need to provide in place of these
        # empty string values that are defined as placeholders.
        #
        # See https://vimeo.com/79220146 for a short video that steps you
        # through this process
        #
        # See https://dev.twitter.com/docs/auth/oauth for more information
        # on Twitter's OAuth implementation.


        CONSUMER_KEY = 'RNGs9JfBd1dkwnGwkU5vZUGEa'
        CONSUMER_SECRET = 'cfIYI2x9bi3KBUMTY0NpjfWiZazIQiQY68HAZ3LBAp9qxQFxML'
        OAUTH_TOKEN = '775098653262254080-IOtUeLlET52C0e8T8ALAjlOXPkXuatl'
        OAUTH_TOKEN_SECRET = 'FGp9Mr0T4TOjrpPCUVJqqCNVknUyGsI0HFtCui5TVtNMH'

        # The keyword query
        QUERY = 'donald'

        # The file to write output as newline-delimited JSON documents
        OUT_FILE = QUERY + ".json"


        # Authenticate to Twitter with OAuth

        auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

        # Create a connection to the Streaming API

        twitter_stream = twitter.TwitterStream(auth=auth)


        self.response.write('Filtering the public timeline for "{0}"'.format(QUERY))

        stream = twitter_stream.statuses.filter(track=QUERY)

        # Write one tweet per line as a JSON document.

        with io.open(OUT_FILE, 'w', encoding='utf-8', buffering=1) as f:
            for tweet in stream:
                f.write(unicode(u'{0}\n'.format(json.dumps(tweet, ensure_ascii=False))))
                self.response.write(tweet['text'])






app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/about', AboutHandler),
    ('/twitter', TwitterHandler)
], debug=True)
