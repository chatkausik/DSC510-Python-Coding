class Bill:
    """
    Object that contains data about of Bill,
    total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a Flatmate Class who lives in a flat
    and share the bill.
    """

    def __init__(self, name, days_in_house):
        self.days_in_house = days_in_house
        self.name = name

    def pays(self, bill, flatmate2):
        return round(bill.amount * self.days_in_house /(self.days_in_house +
                                                  flatmate2.days_in_house), 2)
