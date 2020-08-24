import openpyxl as xl
from CommandDecorator import *
from config import *

import json


def read_TableDefinition(excelDir):
    book = xl.load_workbook(excelDir)

    questions = listQ(
        message="Select Sheet >> ", name="sheet", choicelist=book.sheetnames,
    )
    answer = prompt(questions, style=style)
    sheet = book[answer.get("sheet")]

    definition_data = []
    table_data = {}
    properties = {}
    for cell in sheet[ITERABLE_COLUMN]:
        if cell.value == TABLE_ID_PROPERTY:
            if len(table_data) > 0:
                table_data["properties"] = properties
                definition_data.append(table_data)
                table_data = {}
                properties = {}
            table_data["id"] = sheet[TABLE_ID_COLUMN + str(cell.row)].value
        elif str(cell.value).isdigit():
            properties[sheet[VALUE_COLUMN + str(cell.row)].value] = ""
    else:
        table_data["properties"] = properties
        definition_data.append(table_data)
    print(json.dumps(definition_data, ensure_ascii=False, indent="\t"))

    with open(
        "./json_dest/" + DEST_JSON_FILENAME + ".json", "w", encoding="utf-8"
    ) as make_file:
        data = json.dumps(definition_data, ensure_ascii=False, indent="\t")
        make_file.write(data)

    input()
