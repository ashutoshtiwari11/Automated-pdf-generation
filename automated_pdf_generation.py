# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 12:45:18 2023

@author: marshal
"""

fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}


from reportlab.platypus import SimpleDocTemplate
report = SimpleDocTemplate("./automated_pdf_generation.pdf")

#created a simple object-report of class 
#this will end up generating the files in pdf form with the name in same folder .

from reportlab.platypus import Paragraph, Spacer, Table, Image
#note that table images etc. are all clases that generates elements of page layout using html css js etc like charaterstics

from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()

title=Paragraph("----------- ----- Automated pdf generation------- ---------   Inventory of my favourite fruits.", styles['h1'])

#to use the table genertion we must have our data in list of list formats

table_data=[]
for i, j in fruit.items():
    table_data.append([i,j])
    
print(table_data)

#adding data to our pdf

report_table =Table(data=table_data)
#report.build([title, report_table]) -- final report will add more feature so read on..

#remember that updting a pdf is not possible every time you use report.bbuild a new pdf is created replacing all data of previos ones.

#adding grphics to our pdf

from reportlab.graphics.shapes  import Drawing
from reportlab.graphics.charts.piecharts import Pie

report_pie = Pie(width=8, height=8)

report_pie.data=[]
report_pie.labels=[]
#note that it takes two lists labels and data 

for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)
    
print(report_pie.data)
print(report_pie.labels)

report_chart=Drawing() #creating an object of class.
report_chart.add(report_pie)

author=Paragraph(" author: Ashutosh tiwari ashutoshtiwari6143@gmail.com", styles["h5"])

report.build([title, report_table, report_chart, author])

print("Thnk you for using our automated products kindly check the file in pdf \n : Automated_pdf_generation.pdf \n  Search in you users diretory. \n author: Ashutosh tiwari ashutoshtiwari6143@gmail.com")

    












