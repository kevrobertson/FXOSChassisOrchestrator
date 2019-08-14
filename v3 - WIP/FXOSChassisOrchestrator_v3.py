import xlrd
import sys
from xlrd.sheet import ctype_text

sys.stdout = open("FXOS_Config.txt", "w")

def dns_servers(localFunction):
    print("scope system")
    print(" scope services")
    print("  create dns %s" % localFunction[1])
    return 1

def ntp_servers(localFunction):
    print ("scope system")
    print (" scope services")
    print ("  create ntp-server %s" % localFunction[1])
    if localFunction[2] != '':
        print ("  set ntp-sha1-key-string %s" % int(localFunction[2]))
        print ("%s" % localFunction[3])
        print ("  exit")
        print (" enable ntp-authentication")

dynDispatch = {
    'dns': dns_servers,
    'ntp': ntp_servers
}

wb = xlrd.open_workbook('Spreadsheet.xlsx')

for i, ws in enumerate(wb.sheets()):
    print("\n~~~~~~~~~~~~~~~~~~~~~~\n %s \n~~~~~~~~~~~~~~~~~~~~~~" % ws.name)
    for row in range(ws.nrows)[0:]:
        rv = ws.row_values(row)
        callThis = rv[0].lower()
        if callThis in dynDispatch:
            dynDispatch[callThis](rv)
