from requests import Session
from allure import step
import logging
import curlify


class EntySession(Session):

    def __init__(self, **kwargs):
        self.base_url = kwargs.pop("base_url")
        super().__init__()

    def post(self, **kwargs):
        return super().post(self.base_url, **kwargs)

    def request(self, method, url, **kwargs):
        graphql_operation = kwargs.get("json").get("query").partition(" ")[0]
        with step(f"{graphql_operation}  {url}"):
            response = super().request(method, url, **kwargs)
            logging.info(curlify.to_curl(response.request))
            logging.info(response.status_code)
            logging.info(response.json())
        return response
