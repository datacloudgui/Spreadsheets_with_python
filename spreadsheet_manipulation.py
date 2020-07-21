import openpyxl

wb = openpyxl.load_workbook('coordenadas.xlsx')
print(type(wb))

sheet = wb.get_sheet_by_name('Hoja1')

print(dir(sheet))

for row in range(2, sheet.max_row +1):
    print(sheet['A' + str(row)].value)