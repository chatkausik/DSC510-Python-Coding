import webbrowser

from fpdf import FPDF


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


class PdfReport:
    """
    Generates a PDF report starting the names of the flatmates, the period, 
    and how much each of them had to pay.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1,
                 flatmate2, bill):

        pdf = FPDF(orientation="P", unit='pt', format='A4')
        pdf.add_page()

        # Add image
        pdf.image("house.png", w=30, h=30)

        # Insert Title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align='C', ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and bill
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=20, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=20, txt=str(round(flatmate1.pays(bill,flatmate2),2)), border=0, ln=1)

        pdf.cell(w=100, h=20, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=20, txt=str(round(flatmate2.pays(bill,flatmate1),2)), border=0, ln=1)

        pdf.output(self.filename)

        webbrowser.open(self.filename)


'''

bill = Bill(120, "June 2022")
john = Flatmate("John",20)
marry = Flatmate("Marry", 25)

print(f"John pays {john.pays(bill,marry)}.")
print(f"Marry pays {marry.pays(bill, john)}.")

pdf_report = PdfReport("bill.pdf")
pdf_report.generate(john, marry, bill)

'''
# CLI Implementation
bill_amt = float(input("Hey user, enter the bill amount: "))
bill_period = input("Hey user, enter billing period: ")

bill = Bill(bill_amt, bill_period)

mate_1_name = input("Enter Flatmate 1 name : ")
mate_1_days = int(input("Enter Flatmate 1 days of stay : "))

mate_2_name = input("Enter Flatmate 2 name : ")
mate_2_days = int(input("Enter Flatmate 2 days of stay : "))

mate_1 = Flatmate(mate_1_name, mate_1_days)
mate_2 = Flatmate(mate_2_name, mate_2_days)

pdf_report = PdfReport("bill_to_pay.pdf")
pdf_report.generate(mate_1, mate_2, bill)

print(f"{mate_1.name} pays {mate_1.pays(bill,mate_2)}.")
print(f"{mate_2.name} pays {mate_2.pays(bill,mate_1)}.")






