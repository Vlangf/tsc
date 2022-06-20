import os

telegram_token = os.getenv('TELEGRAM_TOKEN')
telegram_webhook_url = os.getenv('TELEGRAM_WEBHOOK_URL')

proxy_type = os.getenv('TELEGRAM_PROXY_TYPE')
proxy_login = os.getenv('TELEGRAM_PROXY_LOGIN')
proxy_password = os.getenv('TELEGRAM_PROXY_PASSWORD')
proxy_host = os.getenv('TELEGRAM_PROXY_HOST')
proxy_port = os.getenv('TELEGRAM_PROXY_PORT')
