import unittest
from pprint import pprint
from mock import patch, Mock
from careerbuilder_api import CareerBuilderApi
from dice_api import DiceApi
from test_assets.joblisting import CAREERBUILDER_API_JOB_DESC, DICE_HTML

class JobListingApiTestCase(unittest.TestCase):
    def test_careerbuilder_api(self):
        COMPANY_NAME = "Vonage"
        patcher = patch('careerbuilder_api.requests')
        self.mock_response = Mock(status_code=200)
        self.mock_response.raise_for_status.return_value = None
        self.mock_response.json.return_value = {
            "ResponseJob": {
                "Job": {
                    "Company": COMPANY_NAME,
                    "CompanyDID": "CHQ5NT6RW4VL0TMN2GT",
                    "DID": "J360ZL62W28W05BK60C",
                    "JobDescription": CAREERBUILDER_API_JOB_DESC,
                    "JobTitle": "Sales Development Representative  - Inside Sales",
                    "LocationCity": "Atlanta",
                    "LocationCountry": "US",
                    "LocationState": "GA",
                }
            }
        }
        self.mock_requests = patcher.start()
        self.mock_requests.get.return_value = self.mock_response
        api = CareerBuilderApi()
        response = api.parse_job('https://www.careerbuilder.com/job/JHS7JG5W84MZZ9V2STM')
        pprint(response)
        self.assertEqual(COMPANY_NAME, response['company'])

    def test_dice_api(self):
        COMPANY_NAME = 'First Republic Bank'
        patcher = patch('careerbuilder_api.requests')
        self.mock_response = Mock(status_code=200)
        self.mock_response.raise_for_status.return_value = None
        self.mock_response.return_value = DICE_HTML
        self.mock_requests = patcher.start()
        self.mock_requests.get.return_value = self.mock_response
        api = DiceApi('https://www.dice.com/jobs/detail/Software-Engineer/90780659/5500')
        response = api.parse_job()
        pprint(response)
        self.assertEqual(COMPANY_NAME, response['company'])

if __name__ == '__main__':
    unittest.main()