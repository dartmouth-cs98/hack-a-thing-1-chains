# Python implementation of a very basic blockchain
# CS98 Jeong Tae Bang

def add_list():
    chain.append([chain[-1], 3.2])
    print chain

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

""" Gather Inputs """
def get_transaction_value():
   user_value = float(input('Enter your transaction amount '))
   return user_value

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
        # tampered or not?
       elif block[0] == chain[index - 1]:
           valid = True
       else:
           valid = False
           break
       index += 1
   return valid


if __name__ == "__main__":
    chain = []

    while True:
        print("Choose an option")
        print('Choose 1 for adding a new transaction')
        print('Choose 2 for printing the blockchain')
        print('Choose 3 if you want to manipulate the data')
        print('Choose anything else if you want to quit')

        user_choice = get_user_choice()

        if user_choice == 1:
            tx_amount = get_transaction_value()
            add_value(tx_amount, get_last_value())
        elif user_choice == 2:
            print_block()
        elif user_choice == 3: # this will cause the loop to break
            if len(chain) >= 1:
                chain[0] = 2
        else:
            break

        if not verify_chain():
            print('Blockchain manipulated')
            break
