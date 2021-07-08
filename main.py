import uuid
import os
import string
import json


class Chain:
    blocs = []


class Wallet (object):
    unique_id = string
    balance = int
    history = []

    def generate_unique_id(self):
        id_unique = uuid.uuid4()

    def __init__(self, solder):
        self.solder = float(solder)

    def add_balance(self, somme):
        self.solder += somme
        return self.solder

    def sub_balance(self, somme):
        self.solder -= somme
        return self.solder

    def send(self, sender, receiver, amount):
        self.current_data.append({

            'sender': sender,

            'receiver': receiver,

            'amount': amount

        })

        return True

    @app.route('/content/wallets', methods=['GET'])
    def save(self):
        wallet = json.dumps(Wallet.unique_id)

    def load(self):
        user = open(Wallet.unique_id)
        data = json.load(user)

        user.close()
class Block:
