import xlrd
import sys

sys.stdout = open("FXOS_Config.txt", "w")

def dns_servers(localFunction):
    print("scope system")
    print(" scope services")
    print("  create dns %s" % localFunction[1])

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

def syslog_local(localFunction):
    print("scope monitoring")
    print(" %s syslog console" % localFunction[1])
    print(" set syslog console level %s" % localFunction[2])
    print(" %s syslog monitor" % localFunction[3])
    print(" set syslog monitor level %s" % localFunction[4])
    print(" %s sylog file" % localFunction[5])
    print(" set syslog file name %s" % localFunction[6])
    print(" set syslog file level %s" % localFunction[7])
    print(" set syslog file size %s" % localFunction[8])

def syslog_servers(localFunction):
    print("scope monitoring")
    print(" enable syslog remote-destination %s" % localFunction[1])
    print(" set syslog remote-destination %s level %s" % (localFunction[1], localFunction[2]))
    print(" set syslog remote-destination %s hostname %s" % (localFunction[1], localFunction[3]))
    print(" set syslog remote-destination %s facility %s" % (localFunction[1], localFunction[4]))

def syslog_local_sources(localFunction):
    print("scope monitoring")
    if localFunction[1] == 'enable':
        print(" enable syslog source faults")
    if localFunction[2] == 'enable':
        print(" enable syslog source audits")
    if localFunction[3] == 'enable':
        print(" enable syslog source events")

def radius(localFunction):
    print("scope security")
    print(" scope radius")
    print("  create server %s" % localFunction[1])
    print("   set authport %s" % int(localFunction[2]))
    print("   set key")
    print("%s" % localFunction[3])
    print("%s" % localFunction[3])
    print("   set order %s" % int(localFunction[4]))
    print("   set retries %s" % int(localFunction[5]))
    print("   set timeout %s" % int(localFunction[6]))

def tacacs(localFunction):
    print("scope security")
    print(" scope tacacs")
    print("  create server %s" % localFunction[1])
    print("   set port %s" % int(localFunction[2]))
    print("   set key")
    print("%s" % localFunction[3])
    print("%s" % localFunction[3])
    print("   set order %s" % int(localFunction[4]))
    print("   set timeout %s" % int(localFunction[5]))

def https_access(localFunction):
    print("scope security")
    print(" scope services")
    print("  create ip-block %s %s https" % (localFunction[1], int(localFunction[2])))
    if localFunction[1] != '':
        print("scope system")
        print(" scope services")
        print("  delete ip-block 0.0.0.0 0 https")

def ssh_access(localFunction):
    print("scope security")
    print(" scope services")
    print("  create ip-block %s %s ssh" % (localFunction[1], int(localFunction[2])))
    if localFunction[1] != '':
        print("scope system")
        print(" scope services")
        print("  delete ip-block 0.0.0.0 0 ssh")

def snmp_access(localFunction):
    print("scope security")
    print(" scope services")
    print("  create ip-block %s %s snmp" % (localFunction[1], int(localFunction[2])))
    if localFunction[1] != '':
        print("scope system")
        print(" scope services")
        print("  delete ip-block 0.0.0.0 0 snmp")

def interfaces(localFunction):
    print("scope eth-uplink")
    print(" scope fabric a")
    print("  enter interface %s" % localFunction[1])
    print("  %s" % localFunction[2])
    print("  set port-type %s" % localFunction[3])
    print("  set auto-negotiation %s" % localFunction[4])
    print("  set admin-speed %s" % localFunction[5])
    print("  set admin-duplex %s" % localFunction[6])

dynDispatch = {
    'dns': dns_servers,
    'ntp': ntp_servers,
    'snmp': snmp_properties,
    'snmp trap': snmp_traps,
    'syslog local': syslog_local,
    'syslog server': syslog_servers,
    'syslog local sources': syslog_local_sources,
    'radius': radius,
    'tacacs': tacacs,
    'tacacs+': tacacs,
    'https acl': https_access,
    'ssh acl': ssh_access,
    'snmp acl': snmp_access,
    'interface': interfaces
}

wb = xlrd.open_workbook('Spreadsheet.xlsx')

for i, ws in enumerate(wb.sheets()):
    print("\n~~~~~~~~~~~~~~~~~~~~~~\n %s \n~~~~~~~~~~~~~~~~~~~~~~" % ws.name)
    for row in range(ws.nrows)[0:]:
        rv = ws.row_values(row)
        callThis = rv[0].lower()
        if callThis in dynDispatch:
            dynDispatch[callThis](rv)

