import http.client

class ServerClient(object):

    def __init__(self, website_url: str):
        self.website_url = website_url

    def sendPOST(self, suburl: str, data: str, headers: str) -> str:
        connection = http.client.HTTPConnection(self.website_url)
        full_url = self.website_url + suburl
        connection.request('POST', full_url, data, headers)
        response = connection.getresponse()
        return response.read().decode()
