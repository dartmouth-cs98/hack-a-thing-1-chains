# Python implementation of a very basic blockchain
# CS98 Jeong Tae Bang

import hashlib
import json

owner = 'JTBang'

def add_list():
    chain.append([chain[-1], 3.2])
    print (chain)

def get_last_value():
    """extract the last element of the blockchain
       first block will have last transaction of 1"""
    if len(chain) == 0:
        return [1]
    return(chain[-1])

def add_value(transaction_amt, last_transaction):
    """the value of the transaction in the last block will
       be put on the new block with the new transaction amount"""
    chain.append([last_transaction, transaction_amt])

# refactored the above version with hashing feature added
def add_value(recipient, sender=owner, amount=1.0):
    transaction = {'sender': sender,
                   'recipient': recipient,
                   'amount': amount
                   }
    open_transactions.append(transaction)

""" Gather Inputs """
def get_transaction_value():
   tx_recipient = input('Enter the recipient of the transaction: ')
   tx_amount = float(input('Enter your transaction amount '))
   return tx_recipient, tx_amount

# Options = {1, 2, 3}
def get_user_choice():
   user_input = input("Please give your choice here: ")
   return user_input



def print_block():
   for block in chain:
       print("Here is your block")
       print(block)


"""A blockchain must be immutable
   Without a hash function, we are checking whether each node contains
   the data of the last transaction"""
def verify_chain():
   index = 0
   valid = True
   for block in chain:
       if index == 0:
           index += 1
           continue
       elif block[0] == chain[index - 1]:
           valid = True
       else:
           valid = False
           break
       index += 1
   return valid

# convert block from dictionary (json) to string (encoded) for hashing
# hashed result is converted back to a string (that we can read)
def hash_block(block):
    return hashlib.sha256(json.dumps(block).encode()).hexdigest()

# The chain will only accept the block if the first two letters of its hash is '00'
def valid_proof(transactions, last_hash, nonce):
    guess_str = str(transactions) + str(last_hash) + str(nonce)
    guess = guess_str.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    print(guess_hash)
    return guess_hash[0:2] == '00'


"""Proof of Work: Difficulty simulated
   This method will return only when we have a valid hash that 
   can be accepted by the chain"""
def pow():
    last_block = chain[-1]
    last_hash = hash_block(last_block)
    nonce = 0
    while not valid_proof(open_transactions, last_hash, nonce):
        nonce += 1
    return nonce

"""We get a hash of the last block and a nonce that will get the 
   new block's hash accepted. Once this is done, generate a reward
   transaction and add the new block to the chain"""
def mine_block():
    last_block = chain[-1]
    hashed_block = hash_block(last_block)
    nonce = pow()
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': reward
    }

    open_transactions.append(reward_transaction)
    block = {
        'prev_hash': hashed_block,
        'index': len(chain),
        'transaction': open_transactions,
        'nonce': nonce
    }
    chain.append(block)

if __name__ == "__main__":
    reward = 10.0
    genesis_block = {
        'prev_hash': '',
        'index': 0,
        'transaction': [],
        'nonce': 23 # dummy value
    }
    chain = [genesis_block]
    open_transactions = []

    while True:
        print("Choose an option")
        print('Choose 1 for adding a new transaction')
        print('Choose 2 for mining a new block')
        print('Choose 3 if you want to print the blockchain')
        print('Choose anything else if you want to quit')

        user_choice = get_user_choice()

        if user_choice == 1:
            tx_data = get_transaction_value()
            recipient, amount = tx_data
            add_value(recipient, amount=amount)
            print(open_transactions)
        elif user_choice == 2:
            mine_block()
        elif user_choice == 3: # this will cause the loop to break
            print_block()
        else:
            break
