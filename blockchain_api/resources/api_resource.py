# -*- Coding: UTF-8 -*-
from uuid import uuid4
import json
import falcon

from blockchain_api.blockchain import blockchain as bc

node_identifire = str(uuid4()).replace('-', '')
blockchain = bc.Blockchain()


class Mine(object):

    def on_get(self, req, resp):
        last_block = blockchain.last_block
        last_proof = last_block['proof']
        proof = blockchain.proof_of_work(last_proof)

        blockchain.new_transaction(
            sender='0',
            recipient=node_identifire,
            amount=1,
        )

        block = blockchain.new_block(proof)

        response = {
            'message': 'New Block Forged',
            'index': block['index'],
            'transactions': block['transactions'],
            'proof': block['proof'],
            'previous_hash': block['previous_hash']
        }
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(response)


class NewTransaction(object):

    def on_post(self, req, resp):
        values = json.loads(req.stream.read().decode('utf-8'))

        required = ['sender', 'recipient', 'amount']
        if not all(k in values for k in required):
            msg = "Missing values"
            resp.status = falcon.HTTP_400
            resp.body = json.dumps({'message': msg})

        index = blockchain.new_transaction(
            sender=values['sender'],
            recipient=values['recipient'],
            amount=values['amount']
        )

        response = {'message': f'Transaction will be added to Block {index}'}
        resp.status = falcon.HTTP_201
        resp.body = json.dumps(response)


class FullChain(object):

    def on_get(self, req, resp):
        response = {
            'chain': blockchain.chain,
            'length': len(blockchain.chain),
        }
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(response)
