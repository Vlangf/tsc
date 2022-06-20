from utils.rest_client import RestClient
from utils.models import WebhookSetOrDelete, WebhookInfo, Update, Message
from utils import settings


class TelegaBot:

    def __init__(self):
        self.rest_client = RestClient(host=f'https://api.telegram.org/bot{settings.telegram_token}',
                                      proxies=self.set_proxy())

    @staticmethod
    def set_proxy() -> dict:
        if settings.proxy_type:
            proxy_result: str = settings.proxy_type
            if settings.proxy_login:
                proxy_result += f'{settings.proxy_login}:{settings.proxy_password}@'
            proxy_result += f'{settings.proxy_host}:{settings.proxy_port}'
            return {'http': proxy_result, 'https': proxy_result}

    def set_webhook(self) -> WebhookSetOrDelete:
        method: str = '/setWebhook'
        response = self.rest_client.post(path=method, params={'url': settings.telegram_webhook_url})

        return WebhookSetOrDelete(**{'result': response.json()})

    def get_webhook_info(self) -> WebhookInfo:
        method: str = '/getWebhookInfo'
        response = self.rest_client.get(path=method)

        return WebhookInfo(**response.json())

    def delete_webhook(self) -> WebhookSetOrDelete:
        method: str = '/deleteWebhook'
        response = self.rest_client.get(path=method)

        return WebhookSetOrDelete(**{'result': response.json()})

    def get_chat_id(self) -> int:
        method: str = '/getUpdates'
        last_update_info: Update = Update(**self.rest_client.get(method).json())

        return last_update_info.result[0].message.chat.id

    def send_message(self, message: str, chat_id, dis_preview: bool = True, parse_mode: str = None,
                     dis_notification: bool = False) -> Message:
        method: str = '/sendMessage'

        json = {
            'chat_id': chat_id,
            'text': message,
            'disable_web_page_preview': dis_preview,
            'parse_mode': parse_mode,
            'disable_notification': dis_notification
        }

        return Message(**self.rest_client.post(method, json=json).json()['result'])
