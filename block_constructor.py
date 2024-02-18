import csv


class BlockConstructor:

    '''Block Constructor Challenge.
        - This Progam reads a CSV file and constructs a valid block off the file.
    '''

    def __init__(self, weight):
        self.weight = weight
 

    def read_mempool_csv(self):
        '''This method reads the CSV file and returns the data
        '''
        mempool_transactions = []
        try:
            with open('mempool.csv', mode='r') as file:
                csv_file = csv.reader(file)
                for lines in csv_file:
                    for line in lines:
                        mempool_transactions.append(line.split(','))
                        # print(line.split(','))
            return mempool_transactions
        except FileNotFoundError as e:
            print(e)


    def get_highest_transaction_fees(self, mempool_transaction_fees):

        """This method gets the transaction with highest fees, to be included in a block.
            - TODO: Maximize the transaction fee, by selecting the transaction with highest fees 
        """

        highest_transaction_fee = mempool_transaction_fees[0]
        high_fee_transactions = []
        for transaction in mempool_transaction_fees:
            if transaction > highest_transaction_fee:
                highest_transaction_fee = transaction
        
        high_fee_transactions.append(highest_transaction_fee)
        print(high_fee_transactions)


    def construct_block(self):

        """This method constructs a valid block, maximizing the transaction fee and block weight"""

        mempool_transactions = self.read_mempool_csv()
        # transaction_fees = []
        parent_transactions = {}
        block_transactions = []

        for tx_index, transaction in enumerate(mempool_transactions):
            # Get all transactions with a valid parent and store them in a list
            if transaction[3] != "":
                parent_transactions[tx_index] = transaction[3]

        for tx_index, transaction in enumerate(mempool_transactions):
            # Ensures only transactions with valid parents are included in the block
            if transaction[3] != "" and transaction[0] in parent_transactions.values():
                if self.weight > int(transaction[2]):
                    block_transactions.append(parent_transactions[tx_index])
                    block_transactions.append(transaction[0])
                    self.weight -= int(transaction[2])
                else:
                    raise Exception("Maximum block size exceeded. You can't add more transactions to this block.")

        
        for transaction in block_transactions:
            print(transaction)
        # print(block_transactions)



def main():
    max_block_weight = 4000000
    block_constructor = BlockConstructor(max_block_weight)
    block_constructor.construct_block()



if __name__ == "__main__":
    main()
