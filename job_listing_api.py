import urlparse
from base_job_listing_api import JobParseException
from careerbuilder_api import CareerBuilderApi
from dice_api import DiceApi

def parse_job(url):
    try:
        hostname = urlparse.urlparse(url).hostname
    except ValueError:
        return None
    try:
        if hostname == 'www.dice.com':
            api = DiceApi(url)
            response = api.parse_job()
        elif hostname == 'www.careerbuilder.com':
            api = CareerBuilderApi()
            response = api.parse_job(url)
        else:
            raise JobParseException
    except JobParseException:
        return None
    return response
