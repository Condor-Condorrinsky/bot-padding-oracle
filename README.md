# Padding Oracle Attack

An exemplary program presenting The Padding Oracle Attack. Written in Python 3.10.
Utilizes AES 256 bit CBC encryption and Base64 encoding.

### Usage

First you need to launch the server we are trying to attack (assuming you're at
the top of the directory tree):

>
> python bot-padding-oracle/VulnerableServer/server_main.py
> 

Then you can use the main application:

>
> python bot-padding-oracle/MainApp/main.py [-h] [-t] [-e] [-v] SERVER TEXT
> 

Default URL of the attacked server is http://127.0.0.1:5000 (the SERVER argument).
TEXT argument accepts Base64 encoded strings or plaintext (with the -e/--encrypt flag).
You can manually ask the server to encrypt your custom message and then break it,
or use pre-made examples in the *stolen_ciphertext.txt* file.
Further details are shown under the -h/--help flag.

### Authors

- Dumin Konrad

### Literature

Check out the following articles about the Padding Oracle Attack,
which helped me understand the idea and create this program:

- https://www.skullsecurity.org/2013/a-padding-oracle-example
- https://github.com/mpgn/Padding-oracle-attack
- https://robertheaton.com/2013/07/29/padding-oracle-attack
- https://flast101.github.io/padding-oracle-attack-explained
- https://book.hacktricks.xyz/crypto-and-stego/padding-oracle-priv
- https://research.nccgroup.com/2021/02/17/cryptopals-exploiting-cbc-padding-oracles
