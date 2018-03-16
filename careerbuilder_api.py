import urlparse
import os.path
import requests
from base_job_listing_api import JobListingApi, JobParseException

class CareerBuilderApi(JobListingApi):
    # JobID length
    BASE_URL = 'http://api.careerbuilder.com'
    JOB_ENDPOINT = '/v3/job'

    def get_request(self, endpoint, querydict):
        payload = {'outputjson': True}
        payload.update(querydict)
        response = requests.get(self.BASE_URL + endpoint, params=payload)
        if not response.ok:
            raise JobParseException
        response = response.json()
        return response

    def parse_job(self, url):
        path = urlparse.urlparse(url).path
        path_parts = os.path.split(path)
        job_id = path_parts[-1]
        response = self.get_request(self.JOB_ENDPOINT, {'DID': job_id})['ResponseJob']['Job']
        job_title = response.get('JobTitle')
        city = response.get('LocationCity')
        state = response.get('LocationState')
        careerbuilder_id = response.get('CompanyDID')
        company = response.get('Company')
        description = self.html_strip_decode(response.get('JobDescription'))
        return self.format_output(job_id, job_title, city, state, company, description)

