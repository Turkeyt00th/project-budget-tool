class Transaction:
    def __init__(self, amount, category, date, description):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

class BudgetMonth:
    def __init__(self, income, committed_expenses, budgets):
        self.income = income
        self.committed_expenses = committed_expenses
        self.budgets = budgets
        self.transactions = []

    def add_transaction(amount, category, date, description):
        transaction = Transaction(amount, category, date, description)
        self.transactions.append(transaction)
    
    def calculate_spend_by_category(self):
        spend_by_category = {}
        for transaction in self.transactions:
            if transaction.category not in spend_by_category:
                spend_by_category[transaction.category] = 0
            spend_by_category[transaction.category] += transaction.amount
        return spend_by_category
    
    def calculate_remaining_by_category(self):
        remaining_by_category = {}
        spend_by_category = self.calculate_spend_by_category()
        for category, budget in self.budgets.items():
            spent = spend_by_category.get(category, 0)
            remaining_by_category[category] = budget - spent
        return remaining_by_category
    
    def calculate_total_discretionary_left(self):
        total_spent = sum(transaction.amount for transaction in self.transactions)
        total_committed = sum(self.committed_expenses.values())
        discretionary_left = self.income - total_committed - total_spent
        return discretionary_left


