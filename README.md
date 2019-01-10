# hack-a-thing-1-jtbang
An implementation of a simple blockchain.  

It includes support for adding transactions, mining blocks, verifying the chain, and rewarding miners.   
The user can build it using `python3 <filename.py>`   
The program takes user input. Please follow the prompts printed at the console/terminal.   

# What I learned
The basic mechanics of a blockchain:   
What makes up a block: hash of previous block, current block transaction, and nonce  
How to generate a nonce: brute force way to enforce `difficulty`   
How to verify the blockchain and why it is secure (tamper proof)

# What didn't work
     No network protocols: This was a simple simulation so did not have network features such as broadcasting to verify... Network support is needed to make the blockchain truly decentralized.   
     No wallet feature: The wallet is an essnetial feature that I want to explore in the future   
     Defensive programming against mal-input: The input to a new transaction can be tailored carefully to create overload for miners   

# Tutorials followed
https://medium.com/coinmonks/blockchain-for-beginners-what-is-blockchain-519db8c6677a   
http://adilmoujahid.com/posts/2018/03/intro-blockchain-bitcoin-python/