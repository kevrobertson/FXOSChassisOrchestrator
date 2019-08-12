import xlrd

workbook = xlrd.open_workbook('excel_inputs.xlsx')
worksheet = workbook.sheet_by_name('Sheet1')

dns1 = worksheet.cell(2, 1)
dns2 = worksheet.cell(3, 1)
dns3 = worksheet.cell(4, 1)

snmp_community = worksheet.cell(6, 1)
snmp_syscontact = worksheet.cell(7, 1)
snmp_syslocation = worksheet.cell(8, 1)

snmp_trap = worksheet.cell(9, 1)
snmp_port = int(worksheet.cell_value(10, 1))
snmp_version = worksheet.cell(11, 1)
snmp_notificationtype = worksheet.cell(12, 1)

auth_type = worksheet.cell(14, 1)
auth_ip = worksheet.cell(15, 1)
auth_port = int(worksheet.cell_value(16, 1))
auth_key = worksheet.cell(17, 1)
auth_priority = int(worksheet.cell_value(18, 1))
auth_retries = int(worksheet.cell_value(19, 1))
auth_timeout = int(worksheet.cell_value(20, 1))

syslog_name = worksheet.cell(22, 1)
syslog_level = worksheet.cell(23, 1)
syslog_ip = worksheet.cell(24, 1)
syslog_facility = worksheet.cell(25, 1)

timezone_continent = int(worksheet.cell_value(27, 1))
timezone_country = int(worksheet.cell_value(28, 1))
timezone_region = int(worksheet.cell_value(29, 1))

https_access1 = worksheet.cell(32, 1)
https_access2 = worksheet.cell(33, 1)
ssh_access1 = worksheet.cell(34, 1)
ssh_access2 = worksheet.cell(35, 1)
snmp_access1 = worksheet.cell(36, 1)
snmp_access2 = worksheet.cell(37, 1)

https_access1_mask = int(worksheet.cell_value(32, 2))
https_access2_mask = int(worksheet.cell_value(33, 2))
ssh_access1_mask = int(worksheet.cell_value(34, 2))
ssh_access2_mask = int(worksheet.cell_value(35, 2))
snmp_access1_mask = int(worksheet.cell_value(36, 2))
snmp_access2_mask = int(worksheet.cell_value(37, 2))