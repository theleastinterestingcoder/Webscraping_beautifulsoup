Webscraping_beautifulsoup
==========


How to scrape information from a single page using Beautiful Soup (http://www.crummy.com/software/BeautifulSoup/).

Estimated read time: *20 minutes*.

<h3> Scoping out the Data </h3>

This tutorial will be scraping fun facts from snapple's webpage: http://www.snapple.com/real-facts/cap-view

Using Chrome dev tools (right click in the page and choose the `Inspect Element` option), you can examine the HTML/CSS that renders the page:

![Screenshot of Snapple's webpage](https://github.com/theleastinterestingcoder/Webscraping_beautifulsoup/blob/master/resources/snapple_webpage.png)


<h3> Introduction </h3>

Beautiful soup  is a simple yet powerful tool that pulls information from a single webpage. When beautiful soup connects to a webpage, it uses string parsers to breakdown the hiearchy of the webpage into little pieces, and stores that in a special data structure that you can manipulate to find what you want. 

Having some basic knowledge of HTML will be a useful, but not necessary, part of this tutorial. Also, the website is a little bit janky, but trust me, this tool is a commonly used tool to pull information from websites :). 

<h3> Installation </h3>

If you have `pip` (which I strongly recommend that you install for these tutorials), type the following into the command line:

```
pip install beautifulsoup4
```

You can find more details about installation here: http://www.crummy.com/software/BeautifulSoup/#Download



<h3> Getting Executing the script </h3>

To run the tutorial, simply type in:
```
python tutorial.py
```

Snapple's website shuffles which facts it gives you. Each time you run the script, you'll get something different. The output from my program looks something like this:

```

    tutorial.py
   
    Written by: Quan Zhou
    December 25th, 2014
    
    This is a script of how to scrape a webpage from http://www.snapple.com/real-facts/cap-view


----------

Connected to: 
    http://www.snapple.com/real-facts/cap-view

Title of the page: 
    Real Facts | Snapple

All information in <p> HTML tags:
    [u'Mosquitoes have 47 teeth.', u'Mongolians invented lemonade around 1299 A.D.', u'Men get hiccups more than women.', u'There is a town in South Dakota named Tea.', u'President William McKinley had a pet parrot that he named "Washington Post."', u'The first American gold rush happened in North Carolina, not California.', u'More energy from the sun hits Earth every hour than the planet uses in a year.', None, None, u"We've sent an email with instructions to create a new password. Your existing password has not been changed.", None]



Fun fact: 
    Mosquitoes have 47 teeth.

More facts:
    Mosquitoes have 47 teeth.
    Mongolians invented lemonade around 1299 A.D.
    Men get hiccups more than women.
    There is a town in South Dakota named Tea.
    President William McKinley had a pet parrot that he named "Washington Post."
    The first American gold rush happened in North Carolina, not California.
    More energy from the sun hits Earth every hour than the planet uses in a year.
```
<h3> Check out the code </h3>

```python
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

# (1) Connect to the webpage
url  = 'http://www.snapple.com/real-facts/cap-view'     # Snapple facts (hopefully, this won't be broken)
page = urllib2.urlopen(url).read()                      # Connect to webpage, and convert contents into string
soup = BeautifulSoup(page)                       # String -> Soup (special data structure of information)

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
```
<h3> Exploring and Understanding Beautiful Soup </h3>

The best way to understand for beautiful soup is to use `ipython`. Here are some tips to keep in mind while you're trying things out:

* Within `ipython` use the function `type()` to figure kind of data structure your variable is. Example: `type(5) == int`
* Within `ipython` use `dir()` to see the functions associated with that data structure. Example: One of the results of `dir("STRING")` is `lower()`. `"STRING".lower() == "string"`
* The length of an iterator such `list`, `stack`, `ResultSet`, etc can be determined with `len([1 2 3]) == 3`. 

   
Beautiful soup is a *tool() that converts `HTML as string` -> `Beautiful Soup Data structures`. There's a whole familiy of beautiful soup structures that I won't get into, but the ones you'll see the most often are:

* `BeautifulSoup Class` which is the class that the the following two classes inherit 
* `Tag` Class which is a div/p/span/etc that is soup with contents inside (like strings or other div/p/spans/etc) that results. 
* `ResultSet` which is an interator of results (usually of the Tag Class) 



Finally, the following functions are your friends:

* `soup.find()` finds the first element that matches your criteria. Maps Soup -> Tag. Ex: `soup.find('div')` 
* `soup.findAll()` finds the all elements that matches your criteria and returns them as a ResultSet. Maps Soup -> ResultSet of Tag. 
* `tag.string` pulls the string from the tag. Maps `ResultSet`-> String. Protip: make sure you're in the right tag. The information you're looking for might be embedded one more layer down! <



<h3> More information </h3>

Want some useful links?
* Beautiful soup's own documentation is pretty useful and informative.: http://www.crummy.com/software/BeautifulSoup/bs4/doc/
* If you want another tutorial, you can check one out here: http://zevross.com/blog/2014/05/16/using-the-python-library-beautifulsoup-to-extract-data-from-a-webpage-applied-to-world-cup-rankings/

