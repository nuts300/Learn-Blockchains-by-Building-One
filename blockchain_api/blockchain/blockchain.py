# -*- Coding: UTF-8 -*-
from time import time
import json
import hashlib


class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # ジェネシスブロックを作る
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        ブロックチェーンに新しいブロックを作る
        :param proof: <int> プルーフ・オブ・ワークアルゴリズムから得られるプルーフ
        :param previous_hash: (オプション) <str> 前のブロックのハッシュ
        :return: <dict> 新しいブロック
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # 現在のトランザクションリストをセット
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        次に採掘されるブロックに加える新しいトランザクションを作る
        :param sender: <str> 送信者のアドレス
        :param recipient: <str> 受信者のアドレス
        :param amount: <init> 量
        :return: <int> このトランザクションを含むブロックのアドレス
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        ブロックのSHA-256ハッシュを作る
        :param block: <dict> ブロック
        :return: <str>
        """
        # 必ずディクショナリがソートされている必要がある
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof):
        """
        シンプルなプルーフ・オブ・ワークアルゴリズム:
        - hash(pp') の最初の4つが0となるような p' を探す
        - p は前のプルーフ、 p' は新しいプルーフ
        :param last_proof: <int>
        :return: <int>
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        プルーフが正しいかを確認する: hash(last_proof, proof)の最初の4つが0となっている？
        :param last_proof: <int> 前のプルーフ
        :param proof: <int> 現在のプルーフ
        :return: <bool> 正しければ true, そうでなければ false
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()

        return guess_hash[:4] == "0000"
