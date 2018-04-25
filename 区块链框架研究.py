Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> pip install Flask==0.12.2 requests==2.18.4
SyntaxError: invalid syntax
>>> # Blockchain类
>>> class Blockchain(object):
   def __init__(self):
       self.chain = []
       self.current_transactions = []
       
   def new_block(self):
       # Creates a new Block and adds it to the chain
       pass
   
   def new_transaction(self):
       # Adds a new transaction to the list of transactions
       pass
   
   @staticmethod
   def hash(block):
       # Hashes a Block
       pass

   @property
   def last_block(self):
       # Returns the last Block in the chain
       pass
# Blockchain类
# 首先创建一个Blockchain类，在构造函数中创建了两个列表，一个用于储存区块链，一个用于储存交易(任若飞2018.04.05)。

>>> 
>>> #块结构，包含内容：index(索引)、timestamp(时间戳unix类型)、transaction(交易列表)、proof of work(工作量证明机制)
>>> block = {
   'index': 1,
   'timestamp': 1506057125.900785,
   'transactions': [
       {
           'sender': "8527147fe1f5426f9dd545de4b27ee00",
           'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
           'amount': 5,
       }
   ],
   'proof': 324984774000,
   'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}
>>> #简单解释：每个新区块都包含上一个区块的哈希值，以此来保障他的不可篡改性，如果前面区块的哈希值被篡改，后面的区块数据也会相应变动。
>>> 
>>> #加入交易分析
>>> class Blockchain(object):
   ...
   
   def new_transaction(self, sender, recipient, amount):
       """
       生成新交易信息，信息将加入到下一个待挖的区块中
       :param sender: <str> Address of the Sender
       :param recipient: <str> Address of the Recipient
       :param amount: <int> Amount
       :return: <int> The index of the Block that will hold this transaction
       """

       self.current_transactions.append({
           'sender': sender,
           'recipient': recipient,
           'amount': amount,
       })

       return self.last_block['index'] + 1

>>> #该系列（new_transaction）即向列表添加一个新的交易记录，并返回该记录将被添加到的区块的索引，在用户提交交易会用到
>>> 
>>> #创建创世区块
>>> 
