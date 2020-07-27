import json

import requests

from sancaqa.mobile.configs import LOGGER


def pretty_print_request(request):
    """
    pretty print Restful request to API log
    argument is request object
    """
    LOGGER.info('{}\n{}\n\n{}\n\n{}\n'.format(
        '-----------Request----------->',
        request.method + ' ' + request.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items()),
        request.body)
        )


def pretty_print_response(response):
    """
    pretty print Restful response to API log
    argument is response object
    """
    LOGGER.info('{}\n{}\n\n{}\n\n{}\n'.format(
        '<-----------Response-----------',
        'Status code:' + str(response.status_code),
        '\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items()),
        response.text
        ))


def pretty_print_response_json(response):
    """ pretty print response in json format.
        If failing to parse body in json format, print in text.
    """
    try:
        resp_data = response.json()
        resp_body = json.dumps(resp_data,indent=4)
    # if .json() fails, ValueError is raised.
    except ValueError:
        resp_body = response.text
    LOGGER.info('{}\n{}\n\n{}\n\n{}\n'.format(
        '<-----------Response-----------',
        'Status code:' + str(response.status_code),
        '\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items()),
        resp_body
        ))


class API:
    response: requests.Response

    def get(self, url: str, **kwargs):
        response = requests.get(url, **kwargs)
        pretty_print_request(response.request)
        pretty_print_response_json(response)
        self.response = response
        return self

    def post(self, url: str, **kwargs):
        response = requests.post(url, **kwargs)
        pretty_print_request(response.request)
        pretty_print_response_json(response)
        self.response = response
        return self

    def assert_status_code(self, code):
        actual = str(self.response.status_code)
        expected = str(code)
        assert actual == expected, f"Status code {actual} is not as expected {expected}"
        return self
