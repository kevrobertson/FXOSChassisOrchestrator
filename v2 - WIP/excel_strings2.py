import xlrd

workbook = xlrd.open_workbook('excel_inputs2.xlsx')
worksheet = workbook.sheet_by_name('Sheet1')

ethernet11_int = worksheet.cell(1, 1)
ethernet11_enable = worksheet.cell(2, 1)
ethernet11_type = worksheet.cell(3, 1)
ethernet11_autoneg = worksheet.cell(4, 1)
ethernet11_speed = worksheet.cell(5, 1)
ethernet11_duplex = worksheet.cell(6, 1)

