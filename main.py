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
import webapp2 as webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from gae_bingo.gae_bingo import ab_test, bingo

class MainHandler(webapp.RequestHandler):
    def get(self):
	    if ab_test("new button design"):
	        self.response.write('Hello world! <a href="/click">Click Me!</a>')
	    else:
	        self.response.write('Hello world! <a href="/click">Click Here!</a>')
	        
class ReceivingHandler(webapp.RequestHandler):
	def get(self):
		bingo("new button design")
		self.response.write('Thanks!')
			        

app = webapp.WSGIApplication([
    ('/', MainHandler),
    ('/click', ReceivingHandler)
], debug=True)

from gae_bingo.middleware import GAEBingoWSGIMiddleware
app = GAEBingoWSGIMiddleware(app)

def main():
    run_wsgi_app(app)

if __name__ == "__main__":
    main()