import uuid
import requests
import structlog


class RestClient:

    def __init__(self, host: str, headers: dict = None, proxies: dict = None):
        if not host:
            raise AttributeError('Attribute host should not be empty.')
        self.host = host
        self.headers = headers
        self.proxies = proxies
        self.log = structlog.get_logger(self.__class__.__name__).bind(service='api')

    def get(self, path: str, params=None, **kwargs):
        return self._send_request(
            'GET', path,
            params=params,
            **kwargs
        )

    def post(self, path: str, json=None, **kwargs):
        return self._send_request(
            'POST', path,
            json=json,
            **kwargs
        )

    def _send_request(self, method: str, path: str, **kwargs):
        url = f'{self.host}{path}'

        log = self.log.bind(request_id=str(uuid.uuid4()))
        log.msg(
            'request',
            method=method,
            url=url,
            json=kwargs.get('json', None),
            params=kwargs.get('params', None),
            data=kwargs.get('data', None),
            headers=kwargs.get('headers', self.headers),
            proxies=kwargs.pop('proxies', self.proxies),
        )
        response = requests.request(
            method=method,
            url=url,
            headers=kwargs.pop('headers', self.headers),
            proxies=kwargs.pop('proxies', self.proxies),
            **kwargs
        )
        log.msg(
            'response',
            url=response.url,
            status_code=response.status_code,
            text=response.text,
            headers=response.headers,
            elapsed=(response.elapsed.microseconds / 1000),
        )
        return response
