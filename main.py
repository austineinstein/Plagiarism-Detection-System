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
import os
import webapp2
import jinja2
import time
import logging
import boto
import boto.emr
from datetime import datetime

 
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
        loader = jinja2.FileSystemLoader(template_dir), autoescape=True)
        
def doRender(handler, tname, values={}):
    temp = os.path.join(os.path.dirname(__file__), 'templates/' + tname)
    if not os.path.isfile(temp):
            doRender(handler, 'index.htm')
            return
    newval = dict(values)
    newval['path'] = handler.request.path
       
    template = jinja_environment.get_template(tname)
    handler.response.out.write(template.render(newval))
    return True


class BotoHandler(webapp2.RequestHandler):
    just = ''
    def post(self):
        timestamp = time.time()
        BotoHandler.just = "%s" % timestamp + self.request.body
        doRender(self, 'alt.htm', {'data' : BotoHandler.just})
        
    def get(self):
        #BotoHandler.just = self.request.body 
        doRender(self, 'alt.htm', {'data' : BotoHandler.just})
        
class MainPage(webapp2.RequestHandler):
    def get(self):
        path = self.request.path
        doRender(self, path)
         
app = webapp2.WSGIApplication([('/file', BotoHandler), ('/.*', MainPage)], debug=True)