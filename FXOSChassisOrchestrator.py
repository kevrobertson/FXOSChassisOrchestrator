
# Imports all the defined strings from excel document
from excel_strings import *

# This configures the DNS servers and commit-buffers and prints the output to console

dns_server1 = """
scope system
scope services
create dns {}
""".format(dns1.value)

dns_server2 = """
scope system
scope services
create dns {}
""".format(dns2.value)

dns_server3 = """
scope system
scope services
create dns {}
""".format(dns3.value)

snmp_properties = """
scope monitoring
enable snmp
set snmp community
{}
set snmp syscontact {}
set snmp syslocation {}
commit-buffer
""".format(snmp_community.value, snmp_syscontact.value, snmp_syslocation.value)

snmp_trap = """
scope monitoring
enable snmp
create snmp-trap {}
set community {}
set port {}
set version {}
set notificationtype {}
commit-buffer
""".format(snmp_trap.value, snmp_community.value,
           snmp_port, snmp_version.value, snmp_notificationtype.value)

auth_radius = """
scope security
scope {}
create server {}
set authport {}
set key
{}
{}
set order {}
set retries {}
set timeout {}
commit-buffer
""".format(auth_type.value, auth_ip.value, auth_port,
           auth_key.value, auth_key.value, auth_priority,
           auth_retries, auth_timeout)

auth_tacacs = """
scope security
scope {}
create server {}
set key
{}
{}
set order {}
set port {}
set retries {}
set timeout {}
commit-buffer
""".format(auth_type.value, auth_ip.value, auth_key.value,
           auth_key.value, auth_priority, auth_port,
           auth_retries, auth_timeout)

timezone = """
scope system
scope services
set timezone
{}
{}
{}
1
commit-buffer
""".format(timezone_continent, timezone_country, timezone_region)

syslog = """
scope monitoring
enable syslog remote-destination {}
set syslog remote-destination {} level {}
set syslog {} hostname {}
set syslog remote-destination {} facility {}""".format(syslog_name.value,
                                                       syslog_name.value,
                                                       syslog_level.value,
                                                       syslog_name.value,
                                                       syslog_ip.value,
                                                       syslog_name.value,
                                                       syslog_facility.value)

accesslist = """
scope system
scope services
create ip-block {} {} https
scope system
scope services
create ip-block {} {} https
scope system
scope services
create ip-block {} {} ssh
scope system
scope services
create ip-block {} {} ssh
scope system
scope services
create ip-block {} {} snmp
scope system
scope services
create ip-block {} {} snmp
scope system
scope services
delete ip-block 0.0.0.0 0 https
scope system
scope services
delete ip-block 0.0.0.0 0 ssh
scope system
scope services
delete ip-block 0.0.0.0 0 snmp
commit-buffer
""".format(https_access1.value, https_access1_mask,
           https_access2.value, https_access2_mask,
           ssh_access1.value, ssh_access1_mask,
           ssh_access2.value, ssh_access2_mask,
           snmp_access1.value, snmp_access1_mask,
           snmp_access2.value, snmp_access2_mask)

interface11 = """
scope eth-uplink
scope fabric a
enter interface Ethernet1/1
{}
set port-type {}
set auto-negotiation {}
set admin-speed {}
set admin-duplex {}
commit-buffer
""".format(enable11.value, porttype11.value, speed11.value,
           autoneg11.value, duplex11.value)

interface12 = """
scope eth-uplink
scope fabric a
enter interface Ethernet1/1
{}
set port-type {}
set auto-negotiation {}
set admin-speed {}
set admin-duplex {}
commit-buffer
""".format(enable12.value, porttype12.value, speed12.value,
           autoneg12.value, duplex12.value)

interface13 = """
scope eth-uplink
scope fabric a
enter interface Ethernet1/1
{}
set port-type {}
set auto-negotiation {}
set admin-speed {}
set admin-duplex {}
commit-buffer
""".format(enable13.value, porttype13.value, speed13.value,
           autoneg13.value, duplex13.value)

interface14 = """
scope eth-uplink
scope fabric a
enter interface Ethernet1/1
{}
set port-type {}
set auto-negotiation {}
set admin-speed {}
set admin-duplex {}
commit-buffer
""".format(enable14.value, porttype14.value, speed14.value,
           autoneg14.value, duplex14.value)

interface15 = """
scope eth-uplink
scope fabric a
enter interface Ethernet1/1
{}
set port-type {}
set auto-negotiation {}
set admin-speed {}
set admin-duplex {}
commit-buffer
""".format(enable15.value, porttype15.value, speed15.value,
           autoneg15.value, duplex15.value)

interface16 = """
scope eth-uplink
scope fabric a
enter interface Ethernet1/1
{}
set port-type {}
set auto-negotiation {}
set admin-speed {}
set admin-duplex {}
commit-buffer
""".format(enable16.value, porttype16.value, speed16.value,
           autoneg16.value, duplex16.value)

interface17 = """
scope eth-uplink
scope fabric a
enter interface Ethernet1/1
{}
set port-type {}
set auto-negotiation {}
set admin-speed {}
set admin-duplex {}
commit-buffer
""".format(enable17.value, porttype17.value, speed17.value,
           autoneg17.value, duplex17.value)

interface18 = """
scope eth-uplink
scope fabric a
enter interface Ethernet1/1
{}
set port-type {}
set auto-negotiation {}
set admin-speed {}
set admin-duplex {}
commit-buffer
""".format(enable18.value, porttype18.value, speed18.value,
           autoneg18.value, duplex18.value)

interface21 = """
scope eth-uplink
scope fabric a
enter interface Ethernet1/1
{}
set port-type {}
set auto-negotiation {}
set admin-speed {}
set admin-duplex {}
commit-buffer
""".format(enable21.value, porttype21.value, speed21.value,
           autoneg21.value, duplex21.value)

interface22 = """
scope eth-uplink
scope fabric a
enter interface Ethernet1/1
{}
set port-type {}
set auto-negotiation {}
set admin-speed {}
set admin-duplex {}
commit-buffer
""".format(enable22.value, porttype22.value, speed22.value,
           autoneg22.value, duplex22.value)

interface23 = """
scope eth-uplink
scope fabric a
enter interface Ethernet1/1
{}
set port-type {}
set auto-negotiation {}
set admin-speed {}
set admin-duplex {}
commit-buffer
""".format(enable23.value, porttype23.value, speed23.value,
           autoneg23.value, duplex23.value)

interface24 = """
scope eth-uplink
scope fabric a
enter interface Ethernet1/1
{}
set port-type {}
set auto-negotiation {}
set admin-speed {}
set admin-duplex {}
commit-buffer
""".format(enable24.value, porttype24.value, speed24.value,
           autoneg24.value, duplex24.value)

interface25 = """
scope eth-uplink
scope fabric a
enter interface Ethernet1/1
{}
set port-type {}
set auto-negotiation {}
set admin-speed {}
set admin-duplex {}
commit-buffer
""".format(enable25.value, porttype25.value, speed25.value,
           autoneg25.value, duplex25.value)

interface26 = """
scope eth-uplink
scope fabric a
enter interface Ethernet1/1
{}
set port-type {}
set auto-negotiation {}
set admin-speed {}
set admin-duplex {}
commit-buffer
""".format(enable26.value, porttype26.value, speed26.value,
           autoneg26.value, duplex26.value)

interface27 = """
scope eth-uplink
scope fabric a
enter interface Ethernet1/1
{}
set port-type {}
set auto-negotiation {}
set admin-speed {}
set admin-duplex {}
commit-buffer
""".format(enable27.value, porttype27.value, speed27.value,
           autoneg27.value, duplex27.value)

interface28 = """
scope eth-uplink
scope fabric a
enter interface Ethernet1/1
{}
set port-type {}
set auto-negotiation {}
set admin-speed {}
set admin-duplex {}
commit-buffer
""".format(enable28.value, porttype28.value, speed28.value,
           autoneg28.value, duplex28.value)

found_radius = "RADIUS configuration found, server IP is {}".format(auth_ip.value)
found_tacacs = "TACACS configuration found, server IP is {}".format(auth_ip.value)
found_dns1 = "DNS configuration found, first server IP is {}".format(dns1.value)
found_dns2 = "DNS configuration found, second server IP is {}".format(dns2.value)
found_dns3 = "DNS configuration found, third server IP is {}".format(dns3.value)
timezone_continent_americas = "Timezone continent will be Americas"
timezone_country_unitedstates = "Timezone country will be United States"
timezone_region_pacific = "Timezone region will be Pacific"
found_https1 = "HTTPS access restrictions found. Subnet will be {} with a prefix length of {}".format(https_access1.value, https_access1_mask)
found_https2 = "HTTPS access restrictions found. Subnet will be {} with a prefix length of {}".format(https_access2.value, https_access2_mask)
found_ssh1 = "SSH access restrictions found. Subnet will be {} with a prefix length of {}".format(ssh_access1.value, ssh_access1_mask)
found_ssh2 = "SSH access restrictions found. Subnet will be {} with a prefix length of {}".format(ssh_access2.value, ssh_access2_mask)
found_snmp1 = "SNMP access restrictions found. Subnet will be {} with a prefix length of {}".format(snmp_access1.value, snmp_access1_mask)
found_snmp2 = "SNMP access restrictions found. Subnet will be {} with a prefix length of {}".format(snmp_access2.value, snmp_access2_mask)

# Print statements to terminal for confirmation
print()
print("### FXOS Platform Settings ###")
print()
if dns1.value == '':
    print("DNS Server 1 configuration not found")
else:
    print(found_dns1)

if dns2.value == '':
    print("DNS Server 2 configuration not found")
else:
    print(found_dns2)

if dns3.value == '':
    print("DNS Server 3 configuration not found")
else:
    print(found_dns3)

if auth_type.value == 'radius':
    print(found_radius)
else:
    print("RADIUS configuration not found")
if auth_type.value == 'tacacs':
    print(found_tacacs)
else:
    print("TACACS configuration not found")

if auth_type.value == 'radius':
    print(auth_radius, file=open("FXOS_Config.txt", "w"))
if auth_type.value == 'tacacs':
    print(auth_tacacs, file=open("FXOS_Config.txt", "w"))

if timezone_continent == 2:
    print(timezone_continent_americas)

if timezone_country == 49:
    print(timezone_country_unitedstates)

if timezone_region == 21:
    print(timezone_region_pacific)

if https_access1.value == '':
    print("HTTPS restrictions not found")
else:
    print(found_https1)

if https_access2.value == '':
    print("Additional HTTPS restrictions not found")
else:
    print(found_https2)

if ssh_access1.value == '':
    print("SSH restrictions not found")
else:
    print(found_ssh1)

if ssh_access2.value == '':
    print("Aditional SSH restrictions not found")
else:
    print(found_ssh2)

if snmp_access1.value == '':
    print("SNMP restrictions not found")
else:
    print(found_snmp1)

if snmp_access2.value == '':
    print("Additional SNMP restrictions not found")
else:
    print(found_snmp2)

# Output the results to the file FXOS_Config.txt

print(snmp_properties, file=open("FXOS_Config.txt", "a"))

print(snmp_trap, file=open("FXOS_Config.txt", "a"))

if dns1.value == '':
     print()
else:
     print(dns_server1, file=open("FXOS_Config.txt", "a"))

if dns2.value == '':
     print()
else:
     print(dns_server2, file=open("FXOS_Config.txt", "a"))

if dns3.value == '':
    print()
else:
     print(dns_server3, file=open("FXOS_Config.txt", "a"))

print("commit-buffer", file=open("FXOS_Config.txt", "a"))

print(timezone, file=open("FXOS_Config.txt", "a"))

print(syslog, file=open("FXOS_Config.txt", "a"))

print(accesslist, file=open("FXOS_Config.txt", "a"))
print()

print(interface11, file=open("FXOS_Config.txt", "a"))
print(interface12, file=open("FXOS_Config.txt", "a"))
print(interface13, file=open("FXOS_Config.txt", "a"))
print(interface14, file=open("FXOS_Config.txt", "a"))
print(interface15, file=open("FXOS_Config.txt", "a"))
print(interface16, file=open("FXOS_Config.txt", "a"))
print(interface17, file=open("FXOS_Config.txt", "a"))
print(interface18, file=open("FXOS_Config.txt", "a"))
print(interface21, file=open("FXOS_Config.txt", "a"))
print(interface22, file=open("FXOS_Config.txt", "a"))
print(interface23, file=open("FXOS_Config.txt", "a"))
print(interface24, file=open("FXOS_Config.txt", "a"))
print(interface25, file=open("FXOS_Config.txt", "a"))
print(interface26, file=open("FXOS_Config.txt", "a"))
print(interface27, file=open("FXOS_Config.txt", "a"))
print(interface28, file=open("FXOS_Config.txt", "a"))
input('Configuration complete. Press enter key to exit')
