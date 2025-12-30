class Expense:
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def to_dict(self):
        return {
            "Date": self.date,
            "Category": self.category,
            "Amount": self.amount,
            "Description": self.description
        }