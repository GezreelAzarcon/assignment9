from fpdf import FPDF
import json

#fileName = input('Enter Specific JSON File Name: ')
#f = open(fileName)
f = open('assignment9.json')
data = json.load(f)

name = data['name']
age = data['age']
address = data['address']
email = data['email']
objective = data['objective']
education =data['education']
experience = data['experience']
reference1 = data['reference1']
reference2 = data['reference2']
pdf = FPDF('P', 'mm', 'Letter')
pdf.add_page()
pdf.set_font('Times', '', 30)
pdf.cell(0,20, 'RESUME', ln= 1, align= 'C')
pdf.set_font('helvetica', '', 15)
pdf.cell(20,20, '', ln=1)
pdf.cell(0,20, 'Name: ' + name, ln=1)
pdf.cell(0,20, 'Age: ' + str(age), ln=1)
pdf.cell(0,20, 'Address: ' + address, ln=1)
pdf.cell(0,20, 'Email Address: ' + email, ln=1)
pdf.cell(0,20, 'Objective: ' + objective, ln=1)
pdf.cell(0,20, 'Education Status: ' + education, ln=1)
pdf.cell(0,20, 'Experience: ' + experience, ln=1)
pdf.cell(0,20, 'References:  ' + reference1, ln=1)
pdf.cell(0,20, '                     ' +reference2, ln=1)
pdf.output('AZARCON_GEZREEL.pdf')