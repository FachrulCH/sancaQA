import requests
import logging


class APIClient(requests.Session):
    def __init__(self):
        super(APIClient, self).__init__()
        self.hooks['response'].append(self._logging)

    @staticmethod
    def _logging(response: requests.Response, *args, **kwargs):
        logging.info('-----------Request----------->')
        logging.info(f"{response.request.method}: {response.request.url}")
        logging.info(f"Headers: {response.request.headers}")
        if response.request.body is not None:
            logging.info(f"Body: {response.request.body}")

        logging.info('<-----------Response-----------')
        logging.info(f"Status: {response.status_code}, elapsed: {response.elapsed.total_seconds()}s")
        logging.info(f"Headers: {response.headers}")
        if response.text != "":
            logging.info(f"Body: {response.text}")