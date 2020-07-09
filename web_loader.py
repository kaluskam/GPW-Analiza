from bs4 import BeautifulSoup
import requests

# this class gets html from url and extract data
class Loader:

    def __init__(self, url):
        self.url = url

    def get_html(self):
        req = requests.get(self.url)
        self.html = BeautifulSoup(req.content, 'html.parser')
        return self.html

    def get_content_within_tags(self, tag, **kwargs): # kwargs reprezentują atrybuty
        for key, value in kwargs.items():
            if key == 'id':
                return self.html.find(tag, id=value)
            elif key == '_class':
                return self.html.find_all(tag, _class=value)
        return self.html.find_all(tag)
