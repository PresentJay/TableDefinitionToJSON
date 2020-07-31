from openpyxl import *
from CommandDecorator import *



def read_TableDefinition(excelDir):
    book = load_workbook(excelDir)
    
    questions = listQ(
        message="Select Sheet >> ",
        name = "sheet",
        choicelist=book.sheetnames,
    )
    answer = prompt(questions, style=style)
    sheet = book[answer.get('sheet')]
    
    for row in sheet.rows:
        print(row)
        print()
    
    input()