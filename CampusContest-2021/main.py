import uuid
import os
import string
import json
import hashlib
from time import time


class Chain:
    def generate_hash(hash):
        hash = hashlib.sha256("a".encode()).hexdigest()
    
    def verify_hash(last_hash, proof , last_proof):
        guess = f'{last_proof}{proof}{last_hash}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def add_block(self, block):
        if len(self.blocks) > 0:
            block.prev_hash = self.blocks[-1].hash
        block.seal()
        block.validate()
        self.blocks.append(block)
        
    def get_blocks(self):
        string_block = "{}{}{}{}{}".format(self.index, self.proof_number, self.previous_hash, self.data, self.timestamp)

        return hashlib.sha256(string_block.encode()).hexdigest()

    def add_transaction(self):
        
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
        self.data.append({

            'sender': sender,

            'receiver': receiver,

            'amount': amount

        })

        return True

    def save(self):
        try:
            with open('wallets.txt',mode='w') as f:
                savable_chain = [block.__dict__ for block in [Block(blok.index,blok.previous_hash,[tx.__dict__ for tx in blok.transactions],blok.proof,blok.timestamp) for blok in self.__chain]]
                f.write(json.dumps(savable_chain))
                f.write('\n')
                savable_tx = [tx.__dict__ for tx in self.__open_transaction]
                f.write(json.dumps(savable_tx))
                f.write('\n')
                f.write(json.dumps(self.__peer_nodes))
        except:
            print('Saving Failed')

    def load(self):
        try:
            with open('wallets.txt',mode='r') as f:
                file_content = f.readlines()
            blockchain = json.loads(file_content[0][:-1])
            updated_blockchain = []
            for block in blockchain:
                converted_tx = [updated_transactions(tx['sender'],tx['recipent'],tx['signature'],tx['amount']) for tx in block['transactions']]
                updated_block = Block(block['index'],block['previous_hash'],converted_tx,block['proof'],block['timestamp'])
                updated_blockchain.append(updated_block)
            self.chain=updated_blockchain
            open_transaction = json.loads(file_content[1][:-1])
            updated_transactions = []
            for tx in open_transaction:
                updated_transaction = updated_transactions(tx['sender'],tx['recipent'],tx['signature'],tx['amount'])
                updated_transactions.append(updated_transaction)
            self.__open_transaction=updated_transactions
            peer_nodes = json.loads(file_content[2])
            self.__peer_nodes = set(peer_nodes)
        except (IOError,IndexError):
            pass
class Block(object):
    self.base_hash = base_hash
    self.hash = None
    self.parent_hash = parent_hash
    self.transactions = transactions
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.new_block(previous_hash='1', proof=100)

    def generate_hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_transaction(self, sender, recipient, amount):
        transactions = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.transactions.append(transactions)
        return self.last_block['index'] + 1

    def get_transaction(self):


    def get_weight():

    def save(self):
        try:
            with open('blocs.txt',mode='w') as f:
                savable_chain = [block.__dict__ for block in [Block(blok.index,blok.previous_hash,[tx.__dict__ for tx in blok.transactions],blok.proof,blok.timestamp) for blok in self.__chain]]
                f.write(json.dumps(savable_chain))
                f.write('\n')
                savable_tx = [tx.__dict__ for tx in self.__open_transaction]
                f.write(json.dumps(savable_tx))
                f.write('\n')
                f.write(json.dumps(self.__peer_nodes))
        except:
            print('Saving Failed')

    def load(self):
        try:
            with open('blockchain.txt',mode='r') as f:
                file_content = f.readlines()
            blockchain = json.loads(file_content[0][:-1])
            updated_blockchain = []
            for block in blockchain:
                converted_tx = [transactions(tx['sender'],tx['recipent'],tx['signature'],tx['amount']) for tx in block['transactions']]
                updated_block = Block(block['index'],block['previous_hash'],converted_tx,block['proof'],block['timestamp'])
                updated_blockchain.append(updated_block)
            self.chain=updated_blockchain
            open_transaction = json.loads(file_content[1][:-1])
            updated_transactions = []
            for tx in open_transaction:
                updated_transaction = transactions(tx['sender'],tx['recipent'],tx['signature'],tx['amount'])
                updated_transactions.append(updated_transaction)
            self.__open_transaction=updated_transactions
            peer_nodes = json.loads(file_content[2])
            self.__peer_nodes = set(peer_nodes)
        except (IOError,IndexError):
            pass
