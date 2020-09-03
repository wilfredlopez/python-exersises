# https://repl.it/repls/SimilarMerryPostgres#main.py
def diplay_base2(amount: int):
    return format(float(amount), '.2f')


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __repr__(self):
        starsTotal = int((30 - len(self.name)) / 2)
        stars = "*" * starsTotal
        totalStr = diplay_base2(self.get_balance())
        depositString = ''
        for deposit in self.ledger:
            amountStr = diplay_base2(deposit['amount'])[:7]
            desStr = deposit['description'][:23]
            extraLen = len(amountStr) + len(desStr)
            spaceLen = (30 - extraLen)
            emptySpace = " " * spaceLen
            if spaceLen < 0:
                emptySpace = " "
            depositString += desStr + emptySpace + amountStr + "\n"
        return stars + self.name + stars + "\n" + depositString + "Total: " + totalStr

    def deposit(self, amount: int, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: int, description=''):
        total = 0
        enoughFonds = self.check_funds(amount)
        if enoughFonds:
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for deposit in self.ledger:
            balance = balance + deposit['amount']
        return balance

    def transfer(self, amount, category):
        hasEnoughFunds = self.check_funds(amount)
        if not hasEnoughFunds:
            return False
        self.withdraw(amount, "Transfer to "+category.name)
        category.deposit(amount, "Transfer from "+self.name)
        return True

    def check_funds(self, amount):
        total = 0
        for deposit in self.ledger:
            total += deposit['amount']
        if total < amount:
            return False
        return True


def create_spend_chart(categories):
    output = ""
    output += "Percentage spent by category\n"
    percentages = list(reversed([i * 10 for i in range(11)]))
    percentages_len_max = len(str(max(percentages)))

    expenses = []
    expenses_total = 0
    for category in categories:
        totalExpense = 0
        for entry in category.ledger:
            if entry["amount"] < 0:
                totalExpense += abs(entry["amount"])
        expenses.append(totalExpense)
        expenses_total += totalExpense

    expenses_percentages = [
        round(totalExpense / expenses_total * 100) for totalExpense in expenses]

    for percentage in percentages:
        output += str(percentage).rjust(percentages_len_max, " ")
        output += "|"
        for expenses_percentage in expenses_percentages:
            output += " "
            if expenses_percentage >= percentage:
                output += "o"
            else:
                output += " "
            output += " "

        output += " \n"

    output += " " * (percentages_len_max + 1)
    output += "---" * len(categories)
    output += "-\n"

    names = [category.name for category in categories]
    names_len = [len(name) for name in names]
    for index_column in range(max(names_len)):
        output += " " * (percentages_len_max + 1)
        for index_row in range(len(names)):
            output += " "
            try:
                letter = names[index_row][index_column]
            except IndexError:
                output += " "
            else:
                output += letter
            output += " "
        output += " \n"

    return output[:-1]
