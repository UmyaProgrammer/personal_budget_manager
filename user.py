from transactions import Transaction


class User:
    def __init__(self, name):
        self.user_name = name
        self.transaction = Transaction(self.user_name)

    def make_transaction(self):
        self.transaction.make_transaction()


    def get_summary(self):
        self.transaction.get_summary()

    def see_all_transactions(self):
        self.transaction.get_all_transactions()