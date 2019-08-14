import xlrd
import sys

sys.stdout = open("FXOS_Config.txt", "w")

def dns_servers(localFunction):
    print("scope system")
    print(" scope services")
    print("  create dns %s" % localFunction[1])
    return 1

def ntp_servers(localFunction):
    print("scope system")
    print(" scope services")
    print("  create ntp-server %s" % localFunction[1])
    if localFunction[2] != '':
        print("  set ntp-sha1-key-string %s" % int(localFunction[2]))
        print("%s" % localFunction[3])
        print("  exit")
        print(" enable ntp-authentication")

def snmp_properties(localFunction):
    print("scope monitoring")
    print(" enable snmp")
    print(" set snmp syscontact %s" % localFunction[3])
    print(" set snmp syslocation %s" % localFunction[4])
    if localFunction[1] != 'v3':
        print(" set snmp community")
        print("%s" % localFunction[2])
    else:
        print(" create snmp-user %s" % localFunction[5])
        print("%s" % localFunction[6])
        print(" set aes-128 %s" % localFunction[7])
        print(" set priv-password")
        print("%s" % localFunction[8])
        print("%s" % localFunction[8])

def snmp_traps(localFunction):
    print("scope monitoring")
    print(" enable snmp")
    print(" create snmp-trap %s" % localFunction[1])
    print(" set community %s" % localFunction[2])
    print(" set port %s" % int(localFunction[3]))
    print(" set version %s" % localFunction[4])
    print(" set notificationtype %s" % localFunction[5])
dynDispatch = {
    'dns': dns_servers,
    'ntp': ntp_servers,
    'snmp': snmp_properties,
    'snmp trap': snmp_traps
}

wb = xlrd.open_workbook('Spreadsheet.xlsx')

for i, ws in enumerate(wb.sheets()):
    print("\n~~~~~~~~~~~~~~~~~~~~~~\n %s \n~~~~~~~~~~~~~~~~~~~~~~" % ws.name)
    for row in range(ws.nrows)[0:]:
        rv = ws.row_values(row)
        callThis = rv[0].lower()
        if callThis in dynDispatch:
            dynDispatch[callThis](rv)

