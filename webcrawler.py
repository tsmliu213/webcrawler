import urllib2, htmllib, re
from bs4 import BeautifulSoup

def href_is_valid(href):
    if(".com" ) in href and "mailto" not in href:
        return True;
    else:
        return False;

def crawl2(url, depth, listOfLinks):
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
                    crawl2(new_href, depth-1, listOfLinks)

                        
                else:
                    if href not in listOfLinks:
                        print str(depth) + '\t' + href
                        listOfLinks.add(href);
                    if "glassdoor" in href:
                        crawl2(href, depth-1, listOfLinks)

class WebCrawler(object):
    def __init__(self, url):
        self.list_of_links =    set()
        self.url =              url
        self.depth =            2

    def crawl(self, url, depth):
        if(depth != 0):
            self.list_of_links.add(url);
            opener = urllib2.build_opener()
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            page =  opener.open(url)

            soup = BeautifulSoup(page)
            for link in soup.find_all('a', href=True):
                href = link.get('href').encode('utf-8')
                if href_is_valid(href):
                    if href[0] == '/':
                        new_href = 'http://www.glassdoor.com' + href
                        if new_href not in self.list_of_links:
                            print str(depth) + '\t' + new_href
                            self.list_of_links.add(new_href);                   
                        self.crawl(new_href, depth-1)

                            
                    else:
                        if href not in self.list_of_links:
                            print str(depth) + '\t' + href
                            self.list_of_links.add(href);
                        if "glassdoor" in href:
                            self.crawl(href, depth-1)

    def href_is_valid(self, href):
        if(".com" ) in href and "mailto" not in href:
            return True;
        else:
            return False;

    def set_depth(self, new_depth):
        self.depth = new_depth


if __name__ == "__main__":
    url = "http://www.glassdoor.com/index.htm"
    #crawl2(url, 3, set())
    web_crawler = WebCrawler(url)
    web_crawler.crawl(url, 2)


