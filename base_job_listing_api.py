import HTMLParser
from bs4 import BeautifulSoup

class JobParseException(Exception):
    pass

class JobListingApi(object):
    def __init__(self, body=None):
        if body:
            self.soup = BeautifulSoup(body)
        else:
            self.soup = None

    def html_decode(self, message):
        return HTMLParser.HTMLParser().unescape(message)

    def html_strip(self, message):
        soup = BeautifulSoup(message)
        text = soup.get_text()
        return ' '.join(text.split())

    def html_strip_decode(self, message):
        return self.html_strip(self.html_decode(message))

    def find_first_html_element_by_class(self, block, classname):
        return self.soup.find(block, class_=classname)

    def find_html_element_by_id(self, block_id):
        return self.soup.find(id=block_id)

    def get_text_from_html_element_by_id(self, block_id):
        return self.find_html_element_by_id(block_id).text

    def get_text_from_html_element_by_class(self, block, classname):
        return self.find_first_html_element_by_class(block, classname).text

    def format_output(self, job_id, job_title, city, state, company, description):
        return {
            'job_id': job_id,
            'job_title': job_title,
            'city': city,
            'state': state,
            'company': company,
            'description': description
        }