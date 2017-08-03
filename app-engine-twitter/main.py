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
from google.appengine.ext import ndb
import io
import jinja2
import json
from models import Response2
import os
import pprint
from random import choice
import twitter
import webapp2
from responses import below10k
from responses import tenKto25K
from responses import above25K



jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        response_store = self.request.get("responser")
        my_template = jinja_environment.get_template('templates/twitter_shade.html')
        render_data = {}
        render_data["responser"] = response_store
        self.response.write(my_template.render(render_data))
        new_response = Response2(responser = response_store)
        new_response.put()
class AboutHandler(webapp2.RequestHandler):
    def get(self):
        my_template = jinja_environment.get_template('templates/about_page.html')
        self.response.write(my_template.render())



class TwitterHandler(webapp2.RequestHandler):
    def get(self):
        my_template = jinja_environment.get_template('templates/twitter_shade.html')

        # XXX: Go to http://twitter.com/apps/new to create an app and get values
        # for these credentials that you'll need to provide in place of these
        # empty string values that are defined as placeholders.
        #
        # See https://vimeo.com/79220146 for a short video that steps you
        # through this process
        #
        # See https://dev.twitter.com/docs/auth/oauth for more information
        # on Twitter's OAuth implementation.
        response_store = self.request.get("responser")
        my_template = jinja_environment.get_template('templates/twitter_shade.html')
        render_data = {}
        render_data["responser"] = response_store
        # self.response.write(my_template.render(render_data))
        new_response = Response2(responser = response_store)
        new_response.put()

        CONSUMER_KEY = 'RNGs9JfBd1dkwnGwkU5vZUGEa'
        CONSUMER_SECRET = 'cfIYI2x9bi3KBUMTY0NpjfWiZazIQiQY68HAZ3LBAp9qxQFxML'
        OAUTH_TOKEN = '775098653262254080-IOtUeLlET52C0e8T8ALAjlOXPkXuatl'
        OAUTH_TOKEN_SECRET = 'FGp9Mr0T4TOjrpPCUVJqqCNVknUyGsI0HFtCui5TVtNMH'

        # The keyword query
        #QUERY = 'donald'

        # The file to write output as newline-delimited JSON documents
        #OUT_FILE = QUERY + ".json"


        # Authenticate to Twitter with OAuth

        auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

        # Create a connection to the Streaming API

        twitter_stream = twitter.Twitter(auth=auth)
        all_tweets = twitter_stream.statuses.user_timeline(screen_name="realDonaldTrump")
        render_data = {}
        #for tweet in all_tweets:
        #self.response.write(all_tweets[0])

        # render_data['id_str'] = tweet['id_str']
        # render_data['screen_name'] = tweet['user']['screen_name']
        # render_data['all_tweets'] = all_tweets
        # for tweet in all_tweets:
        #     embed = twitter_stream.statuses.oembed(_id=tweet['id_str'])
            # html_list = []
            # render_data['html_list'] = html_list
            # html_list.append(embed)
            #self.response.write(embed)
            # html = twitter_stream.statuses.oembed(embed(tweet['html']))
        retweet_count = all_tweets[0]['retweet_count']

        below = choice(below10k)
        ten = choice(tenKto25K)
        above = choice(above25K)



        if retweet_count <= 9999:
            render_data['responses'] = below
            # self.response.write(my_template.render(render_data['below']))
        elif retweet_count >= 10000 and retweet_count <= 24999:
            render_data['responses'] = ten
            # self.response.write(my_template.render(render_data['ten']))
        elif retweet_count >= 25000:
            render_data['responses'] = above
            # self.response.write(my_template.render(render_data['above']))



            # tweet_text = tweet['text']
            # screen_name = tweet['user']['screen_name']
            # id_str = tweet['id_str']


            # self.response.write("<pre>THIS IS A TWEET::: "  +
            # pprint.pformat(tweet_text) + '\n' +
            # pprint.pformat(screen_name) + '\n' +
            # pprint.pformat(id_str) + '\n' +
            # "\n------</pre>")

        embed_html = twitter_stream.statuses.oembed(_id=all_tweets[0]['id_str'])['html']
        render_data['embed_html'] = embed_html
        self.response.write(my_template.render(render_data))







app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/about', AboutHandler),
    ('/twitter', TwitterHandler)
], debug=True)
