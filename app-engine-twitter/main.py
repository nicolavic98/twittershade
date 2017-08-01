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
import io
import json
<<<<<<< HEAD
#import twitter
=======
# import twitter
<<<<<<< HEAD
>>>>>>> 46c57d13ba4b484a9ca993403475fba369cf0f9c
#from exampletwit import Query
=======
# from exampletwit import Query
>>>>>>> 3b1fbf7f4db2f2d91c8505f78578c705e70e8053

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        my_template = jinja_environment.get_template('templates/twitter_shade.html')
        self.response.write(my_template.render())
class AboutHandler(webapp2.RequestHandler):
    def get(self):
        my_template = jinja_environment.get_template('templates/about_page.html')
        self.response.write(my_template.render())


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/about', AboutHandler)
], debug=True)
