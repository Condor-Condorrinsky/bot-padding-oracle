import http.client


class ServerClient(object):

    def __init__(self, website_url: str):
        self.website_url = website_url

    def send_post(self, sub_url: str, data: str, headers: dict[str: str]) -> str:
        connection = http.client.HTTPConnection(self.website_url)
        connection.request('POST', sub_url, data, headers)
        response = connection.getresponse()
        return response.read().decode()
