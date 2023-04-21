import http.client

class ServerClient(object):

    def __init__(self, website_url: str):
        self.website_url = website_url

    def sendPOST(self, suburl: str, data: str, headers: str):
        connection = http.client.HTTPConnection(self.website_url)
        connection.request('POST', suburl, data, headers)
        response = connection.getresponse()
        return response.read().decode()
