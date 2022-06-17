from Flatmates_Bill.flat import Bill, Flatmate
from Flatmates_Bill.pdfreport import PdfReport
import os

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






