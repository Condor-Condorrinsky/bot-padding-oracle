from flask import Flask, request
from server_logic import *

server = Flask(__name__)

@server.route('/encrypt', methods=['POST'])
def POST_encrypt():
    content = request.json
    return encrypt(content.get('plaintext'))

@server.route('/checkpadding', methods=['POST'])
def POST_check_padding():
    content = request.json
    return str(check_padding(content.get('ciphertext')))

if __name__ == '__main__':
    server.run(host='localhost', port=5000, debug=False)
