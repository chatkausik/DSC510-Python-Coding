# Author: Kausik Chattapadhyay
# DSC 510 Assignment 3.1
# 06/21/2022
# The purpose of this program is to calculate the total cost
# to purchase fiber optic cable and provide a discounted
# price for higher quantities

print('Welcome to FB Optics Fiber Optic Cable Calculator.')

# Requesting user to input their company name
import fpdf

company_name = input('Please enter the name of your company: ')

# Requesting user to input amount of optic cable measured in feet
# while loop will continue until valid value is given
while True:
    try:
        cable_length = float(input('Please enter amount of cable in feet: '))
    except ValueError as ex:
        print(ex)
        continue
    else:
        break

if 100.00 < cable_length <= 250.00:
    cost_per_foot = 0.80
elif 250.00 <= cable_length <= 500.00:
    cost_per_foot = 0.70
elif cable_length > 500.00:
    cost_per_foot = 0.50
else:
    cost_per_foot = 0.87

# cost per foot depending on the amount of feet ordered
total_cost = float(cable_length) * float(cost_per_foot)
print(f"The total rate per foot is ${'{:,.2f}'.format(cost_per_foot)}")
print('Thank you ' + str(company_name) + ' for your order.')

print(f"The quantity of fiber optic cable ordered is {'{:,.2f}'.format(cable_length)}")
print(f"The total cost of your order comes to ${'{:,.2f}'.format(total_cost)}")

# Printing Receipt
print("****** RECiEPT ************************")
print("                                       ")
print(f"Company                  :{company_name}")
print(f"Fiber optic cable length :{'{:,.2f}'.format(cable_length)} feet")
print(f"cable cost per foot      :${'{:,.2f}'.format(cost_per_foot)}")
print(f"Total cost               :${'{:,.2f}'.format(total_cost)}")
print("                                       ")
print("****** Thank you **********************")

# Create PDF receipt
pdf = fpdf.FPDF(orientation="P", unit='pt', format='A4')
pdf.add_page()

# Insert Title
pdf.set_font(family='Times', size=24, style='B')
pdf.cell(w=0, h=80, txt="Fiber Optic Receipt", border=0, align='C', ln=1)

# Insert details
pdf.set_font(family='Times', size=12)
pdf.cell(w=150, h=20, txt="Company                   ", border=0)
pdf.cell(w=150, h=20, txt=str(": " + company_name), border=0, ln=1)

pdf.cell(w=150, h=20, txt="Fiber optic cable length  ", border=0)
pdf.cell(w=150, h=20, txt=str(": "'{:,.2f}'.format(cable_length)), border=0, ln=1)

pdf.cell(w=150, h=20, txt="Cable cost per foot       ", border=0)
pdf.cell(w=150, h=20, txt=str(": "'{:,.2f}'.format(cost_per_foot)), border=0, ln=1)

pdf.cell(w=150, h=20, txt="Total cost                ", border=0)
pdf.cell(w=150, h=20, txt=str(": "'{:,.2f}'.format(total_cost)), border=0, ln=1)

pdf.output("receipt.pdf")
