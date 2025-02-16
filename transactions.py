import pandas
import datetime


def get_date():
    date = datetime.date.today()
    return date




class Transaction:
    def __init__(self, user):
        self.file_location = "data/all_transactions.csv"
        self.user = user


    def make_transaction(self) -> None:
        data = pandas.read_csv(filepath_or_buffer=self.file_location)
        list_of_ids = data['id']

        transaction_id = len(list_of_ids)
        user = self.user
        categories = ["Essentials", "Financial Responsibilities", "Discretionary", "Personal & Family",
                      "Business & Work-Related"]

        category = int(input("Category (1-5): "))
        while category not in range(1, 6):
            category = int(input("Please enter (1-5): "))

        cost = float(input("Cost: "))

        info = {
            "id": [transaction_id],
            "user": [user],
            "category": [categories[category - 1]],
            "cost": [cost],
            "date": [get_date()]
        }

        df = pandas.DataFrame(info)
        df.to_csv(path_or_buf=self.file_location, mode='a', index=False, header=False)



    def get_all_transactions(self):
        data = pandas.read_csv(filepath_or_buffer=self.file_location)
        user_transactions = data[data.user == self.user]
        print('\n')
        print(user_transactions)
        print('\n')

    def get_summary(self):
        data = pandas.read_csv(filepath_or_buffer=self.file_location)
        user_transactions = data[data.user == self.user]

        def get_category_spent(ctg: str) -> float:
            spent = 0
            all_money_spent = user_transactions[user_transactions['category'] == ctg]

            for mny in all_money_spent['cost']:
                spent += float(mny)

            return spent



        total_money = user_transactions['cost'].tolist()
        total_money_spent = 0

        for money in total_money:
            total_money_spent += money

        all_categories = user_transactions['category'].tolist()
        categories = list(set(all_categories))
        categories_and_money_spent = {}

        for category in categories:
            money_spent = get_category_spent(category)
            categories_and_money_spent[f"{category}"] = money_spent

        for key, value in categories_and_money_spent.items():
            print(f"Category: {key}\n\tMoney you spent: {value}\n\tAllocation: %{round(value / total_money_spent, 3) * 100}\n")







        




