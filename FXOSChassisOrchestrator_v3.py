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

def portchannels(localFunction):
    print("scope eth-uplink")
    print(" scope fabric a")
    print("  create port-channel %s" % int(localFunction[1]))
    print("   set port-type %s" % localFunction[2])
    print("   set auto-negotiation %s" % localFunction[3])
    print("   set speed %s" % localFunction[4])
    print("   set duplex %s" % localFunction[5])
    print("   set port-channel-mode %s" % localFunction[6])
    if localFunction[7] == '':
        pass
    else:
        print("   create member-port %s" % localFunction[7])
    if localFunction[8] == '':
        pass
    else:
        print("   create member-port %s" % localFunction[8])
    if localFunction[9] == '':
        pass
    else:
        print("   create member-port %s" % localFunction[9])
    if localFunction[10] == '':
        pass
    else:
        print("   create member-port %s" % localFunction[10])
    if localFunction[11] == '':
        pass
    else:
        print("   create member-port %s" % localFunction[11])
    if localFunction[12] == '':
        pass
    else:
        print("   create member-port %s" % localFunction[12])
    if localFunction[13] == '':
        pass
    else:
        print("   create member-port %s" % localFunction[13])
    if localFunction[14] == '':
        pass
    else:
        print("   create member-port %s" % localFunction[14])

def standalone_asa(localFunction):
    print("scope ssa")
    print(" scope slot %s" % int(localFunction[1]))
    print("  enter app-instance asa %s" % localFunction[2])
    print("   set startup-version %s" % localFunction[3])
    print("   exit")
    print("  exit")
    print(" enter logical-device %s asa %s standalone" % (localFunction[2], int(localFunction[1])))
    print("  create external-port-link %s %s asa" % (localFunction[9], localFunction[10]))
    print('   set description "%s"' % localFunction[11])
    print("   exit")

    if localFunction[12] == '':
        pass
    else:
        print("  create external-port-link %s %s asa" % (localFunction[12], localFunction[13]))
        print('   set description "%s"' % localFunction[14])
        print("   exit")
    if localFunction[15] == '':
        pass
    else:
        print("  create external-port-link %s %s asa" % (localFunction[15], localFunction[16]))
        print('   set description "%s"' % localFunction[17])
        print("   exit")
    if localFunction[18] == '':
        pass
    else:
        print("  create external-port-link %s %s asa" % (localFunction[18], localFunction[19]))
        print('   set description "%s"' % localFunction[20])
        print("   exit")
    if localFunction[21] == '':
        pass
    else:
        print("  create external-port-link %s %s asa" % (localFunction[21], localFunction[22]))
        print('   set description "%s"' % localFunction[23])
        print("   exit")

    print("  create mgmt-bootstrap asa")
    print("   create bootstrap-key FIREWALL_MODE")
    print("    set value %s" % localFunction[4])
    print("    exit")
    print("   create bootstrap-key-secret PASSWORD")
    print("    set value")
    print("%s" % localFunction[5])
    print("%s" % localFunction[5])
    print("    exit")
    print("   create ipv4 %s default" % int(localFunction[1]))
    print("    set ip %s mask %s" % (localFunction[6], localFunction[7]))
    print("    set gateway %s" % localFunction[8])

def standalone_ftd(localFunction):
    print("scope ssa")
    print(" scope app ftd %s" % localFunction[3])
    print("  accept-license-agreement")
    print("")
    print("  commit-buffer")
    print("  exit")
    print(" scope slot %s" % int(localFunction[1]))
    print("  enter app-instance ftd %s" % localFunction[2])
    print("   set deploy-type native")
    print('   set resource-profile-name ""')
    print("   set startup-version %s" % localFunction[3])
    print("   exit")
    print("  exit")
    print(" enter logical-device %s ftd %s standalone" % (localFunction[2], int(localFunction[1])))
    print("  create external-port-link %s %s ftd" % (localFunction[16], localFunction[17]))
    print('   set description "%s"' % localFunction[18])
    print("   exit")

    if localFunction[19] == '':
        pass
    else:
        print("  create external-port-link %s %s ftd" % (localFunction[19], localFunction[20]))
        print('   set description "%s"' % localFunction[21])
        print("   exit")
    if localFunction[22] == '':
        pass
    else:
        print("  create external-port-link %s %s ftd" % (localFunction[22], localFunction[23]))
        print('   set description "%s"' % localFunction[24])
        print("   exit")
    if localFunction[25] == '':
        pass
    else:
        print("  create external-port-link %s %s ftd" % (localFunction[25], localFunction[26]))
        print('   set description "%s"' % localFunction[27])
        print("   exit")
    if localFunction[28] == '':
        pass
    else:
        print("  create external-port-link %s %s ftd" % (localFunction[28], localFunction[29]))
        print('   set description "%s"' % localFunction[30])
        print("   exit")

    print("  create mgmt-bootstrap ftd")
    print("   create bootstrap-key FIREWALL_MODE")
    print("    set value %s" % localFunction[4])
    print("   exit")
    print("  create bootstrap-key FIREPOWER_MANAGER_IP")
    print("   set value %s" % localFunction[9])
    print("   exit")
    print("  create bootstrap-key-secret REGISTRATION_KEY")
    print("   set value")
    print("%s" % localFunction[10])
    print("%s" % localFunction[10])
    print("   exit")
    print("  create bootstrap-key-secret PASSWORD")
    print("   set value")
    print("%s" % localFunction[5])
    print("%s" % localFunction[5])
    print("   exit")
    print("  create bootstrap-key FQDN")
    print("   set value %s" % localFunction[11])
    print("   exit")
    print("  create bootstrap-key DNS_SERVERS")
    print("   set value %s,%s,%s" % (localFunction[12], localFunction[13], localFunction[14]))
    print("   exit")
    print("  create bootstrap-key SEARCH_DOMAINS")
    print("   set value %s" % localFunction[15])
    print("   exit")
    print("   create ipv4 %s default" % int(localFunction[1]))
    print("    set ip %s mask %s" % (localFunction[6], localFunction[7]))
    print("    set gateway %s" % localFunction[8])

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
    'interface': interfaces,
    'port-channel': portchannels,
    'asa': standalone_asa,
    'ftd': standalone_ftd
}

wb = xlrd.open_workbook('Spreadsheet.xlsx')

for i, ws in enumerate(wb.sheets()):
    print("\n~~~~~~~~~~~~~~~~~~~~~~\n %s \n~~~~~~~~~~~~~~~~~~~~~~" % ws.name)
    for row in range(ws.nrows)[0:]:
        rv = ws.row_values(row)
        callThis = rv[0].lower()
        if callThis in dynDispatch:
            dynDispatch[callThis](rv)

