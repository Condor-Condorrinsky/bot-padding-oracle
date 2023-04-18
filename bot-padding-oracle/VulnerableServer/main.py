from flask import Flask, request
from server_logic import *

server = Flask(__name__)

@server.route('/encrypt', methods=['GET'])
def GET_encrypt():
    plain = request.args.get('plaintext')
    return encrypt(plain)

@server.route('/checkpadding', methods=['GET'])
def GET_check_padding():
    ciphertext = request.args.get('ciphertext')
    return check_padding(ciphertext)

if __name__ == '__main__':
    server.run(host='localhost', port=5000, debug=False)
