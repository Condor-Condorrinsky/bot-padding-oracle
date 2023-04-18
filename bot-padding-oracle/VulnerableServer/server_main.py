from flask import Flask, request
from server_logic import *

server = Flask(__name__)

@server.route('/encrypt', methods=['POST'])
def GET_encrypt():
    # plain = request.args.get('plaintext')
    content = request.json
    print(content)
    return encrypt(content.get('cos'))

@server.route('/checkpadding', methods=['POST'])
def GET_check_padding():
    content = request.json
    print(content)
    return str(check_padding(content.get('cos')))

if __name__ == '__main__':
    server.run(host='localhost', port=5000, debug=False)
