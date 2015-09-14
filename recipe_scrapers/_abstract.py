from urllib import request

from bs4 import BeautifulSoup


class AbstractScraper():

    def __init__(self, url, test=False):
        if test:
            # when testing, we simply load a file
            self.soup = BeautifulSoup(url.read(), "html.parser")
        else:
            self.soup = BeautifulSoup(request.urlopen(url).read(), "html.parser")

    def host(self):
        """ get the host of the url, so we can use the correct scraper (check __init__.py) """
        raise NotImplementedError("This should be implemented.")

    def publisher_site(self):
        """ the original url of the publisher site """
        raise NotImplementedError("This should be implemented.")

    def title(self):
        """ title of the recipe itself """
        raise NotImplementedError("This should be implemented.")

    def total_time(self):
        """ total time it takes to preparate the recipe in minutes """
        raise NotImplementedError("This should be implemented.")

    def ingredients(self):
        """ list of ingredients needed for the recipe """
        raise NotImplementedError("This should be implemented.")

    def directions(self):
        """ directions provided on the recipe link """
        raise NotImplementedError("This should be implemented.")

    def social_rating(self):
        """ social rating of the recipe in 0 - 100 scale """
        raise NotImplementedError("This should be implemented.")
