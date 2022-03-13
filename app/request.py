import requests

base_url = None


def configure_request(app):
    global base_url
    base_url = app.config['QUOTE_API_BASE_URL']