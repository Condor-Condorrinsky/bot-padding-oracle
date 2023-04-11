from flask import Flask, request

server = Flask(__name__)

@server.route('/encrypt', methods=['GET'])
def GET_encrypt():
    pass

@server.route('/checkpadding', methods=['GET'])
def GET_check_padding():
    pass

if __name__ == '__main__':
    server.run(host='localhost', port=5000, debug=False)
