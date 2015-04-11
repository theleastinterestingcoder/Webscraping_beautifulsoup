'''
  fact_generator.py

  Written by: Quan Zhou 
  on December 25th, 2014

  Exposes a fact generator as an object. This is a standalone object. 
'''

from bs4 import BeautifulSoup                           # Import to parse HTML structure
import urllib2                                          # Library used to make connections to a webpage

class fact_generator:
    def __init__(self):
        # (0) some spoofing here to trick snapple
        headers = { 'User-Agent' : 'Mozilla/5.0' }                  # Tell other people we're on Firefox
        url  = 'http://www.snapple.com/real-facts/cap-view'     
        self.req = urllib2.Request(url, None, headers)               # Create the request
    def get_fact(self):
        html = urllib2.urlopen(self.req).read()                      # Read the request, as a string
        soup = BeautifulSoup(html)                                   # String -> Soup (special data structure of information)
        fact_div  = soup.find("div", { "class" : "fact_text_wrap" })    # Use ChromeDevTools to uniquely identify this info
        fact_p    = fact_div.find('p')                                  # Get the paragraph buried in the <div> tag
        fact_str  = fact_p.string                                       # Get to your fun fact

        return fact_str

if __name__ == '__main__':
    print __doc__
    # Here's an example of how to use this
    fg = fact_generator()
    print "Fun fact: %s" % fg.get_fact()




