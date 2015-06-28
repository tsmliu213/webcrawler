import urllib2, htmllib, re
from bs4 import BeautifulSoup

def href_is_valid(href):
    if(".com" ) in href and "mailto" not in href:
        return True;
    else:
        return False;

def crawl(url, depth, listOfLinks):
    if(depth != 0):
        listOfLinks.add(url);
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        page =  opener.open(url)

        soup = BeautifulSoup(page)
        for link in soup.find_all('a', href=True):
            href = link.get('href').encode('utf-8')
            if href_is_valid(href):
                if href[0] == '/':
                    new_href = 'http://www.glassdoor.com' + href
                    if new_href not in listOfLinks:
                        print str(depth) + '\t' + new_href
                        listOfLinks.add(new_href);                   
                    crawl(new_href, depth-1, listOfLinks)

                        
                else:
                    if href not in listOfLinks:
                        print str(depth) + '\t' + href
                        listOfLinks.add(href);
                    if "glassdoor" in href:
                        crawl(href, depth-1, listOfLinks)




url = "http://www.glassdoor.com/index.htm"
crawl(url, 3, set())


