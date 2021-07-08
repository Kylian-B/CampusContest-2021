import uuid
import os
import string


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

    def NouveauSolde(self, somme):
        self.solde = float(somme)

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


class Block:
