import urlparse
import os.path
import requests
from base_job_listing_api import JobListingApi, JobParseException

class DiceApi(JobListingApi):
    def __init__(self, url):
        self.url = url
        response = requests.get(url)
        if not response.ok:
            raise JobParseException
        super(DiceApi, self).__init__(response.text)

    def parse_job(self):
        path = urlparse.urlparse(self.url).path
        path_parts = os.path.split(os.path.split(path)[0])
        job_id = path_parts[-1]
        job_title = self.get_text_from_html_element_by_class('h1', 'jobTitle').strip()
        location = self.get_text_from_html_element_by_class('li', 'location').strip()
        split_location = location.split(', ')
        city = split_location[0]
        state = split_location[1]
        company = self.find_first_html_element_by_class('li', 'employer').find('a').text.strip()
        description = self.html_strip(self.get_text_from_html_element_by_id('jobdescSec'))
        return self.format_output(job_id, job_title, city, state, company, description)

