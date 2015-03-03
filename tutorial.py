'''
    tutorial.py
   
    Written by: Quan Zhou
    December 25th, 2014
    
    How to scrape a webpage from http://www.snapple.com/real-facts/cap-view

'''

print(__doc__)
print "-"*10

from bs4 import BeautifulSoup                           # Import to parse HTML structure
import urllib2                                          # Library used to make connections to a webpage

# (0) some spoofing here to trick snapple
headers = { 'User-Agent' : 'Mozilla/5.0' }              # Tell other people we're on Firefox
url  = 'http://www.snapple.com/real-facts/cap-view'     
req = urllib2.Request(url, None, headers)               # Create the request
html = urllib2.urlopen(req).read()                      # Read the request, as a string
soup = BeautifulSoup(html)                              # String -> Soup (special data structure of information)


# (2) Quick aside: Here are some examples of things you might be interested in
titleTag = soup.find("title").string                    #  The title of the page: u'Real Facts | Snapple'
p_soup   = soup.findAll('p')                            #  Grab all the information wrapped in <p> tags
p_info   = [p.string for p in p_soup]                   #     then convert (Result set) -> List of Strings

# (3) Getting to what we want: Look for 'div' tags with class="fact_text_wrap"
fact_div  = soup.find("div", { "class" : "fact_text_wrap" })    # Use ChromeDevTools to uniquely identify this info
fact_p    = fact_div.find('p')                                  # Get the paragraph buried in the <div> tag
fact_str  = fact_p.string                                       # Get to your fun fact

# (4) More stuff: And if you want to grab all the fun facts in one go
more_facts_tags = soup.findAll("div", { "class" : "fact_text_wrap" }) # use findAll(), not find()
more_facts_strs = [div.find('p').string for div in more_facts_tags]   # For each div, look at the paragraph inside, and convert to string


# Let's print out all the information we scraped!
print "\nConnected to: \n\t", url
print "\nTitle of the page: \n\t", titleTag
print "\nAll information in <p> HTML tags:\n\t", p_info
print "\n"
print "\nFun fact: \n\t", fact_str
print "\nMore facts:"
for fact in more_facts_strs:
    print "\t", fact