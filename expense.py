# expense.py
class Expense:
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.description = description

    def to_list(self):
        """Converts object data into a list for CSV storage."""
        return [self.date, self.category, self.amount, self.description]