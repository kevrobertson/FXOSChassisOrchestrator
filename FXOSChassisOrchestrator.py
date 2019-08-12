
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

port_channel1_properties = """
scope eth-uplink
scope fabric a
create port-channel {}
enable
set port-type {}
set auto-negotiation {}
set speed {}
set duplex {}
set port-channel-mode {}
""".format(port_channel1_num, port_channel1_type.value,
           port_channel1_neg.value, port_channel1_speed.value,
           port_channel1_duplex.value, port_channel1_mode.value)

portchannel1_1 = """
create member-port {}
exit
""".format(port_channel1_port1.value)

portchannel1_2 = """
create member-port {}
exit
""".format(port_channel1_port2.value)

portchannel1_3 = """
create member-port {}
exit
""".format(port_channel1_port3.value)

portchannel1_4 = """
create member-port {}
exit
""".format(port_channel1_port4.value)

portchannel1_5 = """
create member-port {}
exit
""".format(port_channel1_port5.value)

portchannel1_6 = """
create member-port {}
exit
""".format(port_channel1_port6.value)

portchannel1_7 = """
create member-port {}
exit
""".format(port_channel1_port7.value)

portchannel1_8 = """
create member-port {}
exit
""".format(port_channel1_port8.value)

portchannel_commit = """
commit-buffer"""


port_channel2_properties = """
scope eth-uplink
scope fabric a
create port-channel {}
enable
set port-type {}
set auto-negotiation {}
set speed {}
set duplex {}
set port-channel-mode {}
""".format(port_channel2_num, port_channel2_type.value,
           port_channel2_neg.value, port_channel2_speed.value,
           port_channel2_duplex.value, port_channel2_mode.value)

portchannel2_1 = """
create member-port {}
exit
""".format(port_channel2_port1.value)

portchannel2_2 = """
create member-port {}
exit
""".format(port_channel2_port2.value)

portchannel2_3 = """
create member-port {}
exit
""".format(port_channel2_port3.value)

portchannel2_4 = """
create member-port {}
exit
""".format(port_channel2_port4.value)

portchannel2_5 = """
create member-port {}
exit
""".format(port_channel2_port5.value)

portchannel2_6 = """
create member-port {}
exit
""".format(port_channel2_port6.value)

portchannel2_7 = """
create member-port {}
exit
""".format(port_channel2_port7.value)

portchannel2_8 = """
create member-port {}
exit
""".format(port_channel2_port8.value)


port_channel3_properties = """
scope eth-uplink
scope fabric a
create port-channel {}
enable
set port-type {}
set auto-negotiation {}
set speed {}
set duplex {}
set port-channel-mode {}
""".format(port_channel3_num, port_channel3_type.value,
           port_channel3_neg.value, port_channel3_speed.value,
           port_channel3_duplex.value, port_channel3_mode.value)

portchannel3_1 = """
create member-port {}
exit
""".format(port_channel3_port1.value)

portchannel3_2 = """
create member-port {}
exit
""".format(port_channel3_port2.value)

portchannel3_3 = """
create member-port {}
exit
""".format(port_channel3_port3.value)

portchannel3_4 = """
create member-port {}
exit
""".format(port_channel3_port4.value)

portchannel3_5 = """
create member-port {}
exit
""".format(port_channel3_port5.value)

portchannel3_6 = """
create member-port {}
exit
""".format(port_channel3_port6.value)

portchannel3_7 = """
create member-port {}
exit
""".format(port_channel3_port7.value)

portchannel3_8 = """
create member-port {}
exit
""".format(port_channel3_port8.value)


port_channel4_properties = """
scope eth-uplink
scope fabric a
create port-channel {}
enable
set port-type {}
set auto-negotiation {}
set speed {}
set duplex {}
set port-channel-mode {}
""".format(port_channel4_num, port_channel4_type.value,
           port_channel4_neg.value, port_channel4_speed.value,
           port_channel4_duplex.value, port_channel4_mode.value)

portchannel4_1 = """
create member-port {}
exit
""".format(port_channel4_port1.value)

portchannel4_2 = """
create member-port {}
exit
""".format(port_channel4_port2.value)

portchannel4_3 = """
create member-port {}
exit
""".format(port_channel4_port3.value)

portchannel4_4 = """
create member-port {}
exit
""".format(port_channel4_port4.value)

portchannel4_5 = """
create member-port {}
exit
""".format(port_channel4_port5.value)

portchannel4_6 = """
create member-port {}
exit
""".format(port_channel4_port6.value)

portchannel4_7 = """
create member-port {}
exit
""".format(port_channel4_port7.value)

portchannel4_8 = """
create member-port {}
exit
""".format(port_channel4_port8.value)


port_channel5_properties = """
scope eth-uplink
scope fabric a
create port-channel {}
enable
set port-type {}
set auto-negotiation {}
set speed {}
set duplex {}
set port-channel-mode {}
""".format(port_channel5_num, port_channel5_type.value,
           port_channel5_neg.value, port_channel5_speed.value,
           port_channel5_duplex.value, port_channel5_mode.value)

portchannel5_1 = """
create member-port {}
exit
""".format(port_channel5_port1.value)

portchannel5_2 = """
create member-port {}
exit
""".format(port_channel5_port2.value)

portchannel5_3 = """
create member-port {}
exit
""".format(port_channel5_port3.value)

portchannel5_4 = """
create member-port {}
exit
""".format(port_channel5_port4.value)

portchannel5_5 = """
create member-port {}
exit
""".format(port_channel5_port5.value)

portchannel5_6 = """
create member-port {}
exit
""".format(port_channel5_port6.value)

portchannel5_7 = """
create member-port {}
exit
""".format(port_channel5_port7.value)

portchannel5_8 = """
create member-port {}
exit
""".format(port_channel5_port8.value)


port_channel6_properties = """
scope eth-uplink
scope fabric a
create port-channel {}
enable
set port-type {}
set auto-negotiation {}
set speed {}
set duplex {}
set port-channel-mode {}
""".format(port_channel6_num, port_channel6_type.value,
           port_channel6_neg.value, port_channel6_speed.value,
           port_channel6_duplex.value, port_channel6_mode.value)

portchannel6_1 = """
create member-port {}
exit
""".format(port_channel6_port1.value)

portchannel6_2 = """
create member-port {}
exit
""".format(port_channel6_port2.value)

portchannel6_3 = """
create member-port {}
exit
""".format(port_channel6_port3.value)

portchannel6_4 = """
create member-port {}
exit
""".format(port_channel6_port4.value)

portchannel6_5 = """
create member-port {}
exit
""".format(port_channel6_port5.value)

portchannel6_6 = """
create member-port {}
exit
""".format(port_channel6_port6.value)

portchannel6_7 = """
create member-port {}
exit
""".format(port_channel6_port7.value)

portchannel6_8 = """
create member-port {}
exit
""".format(port_channel6_port8.value)


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

port_channel1_announce = """Port-channel1 is configured with member interfaces: {} {} {} {} {} {} {} {}""".format(port_channel1_port1.value, port_channel1_port2.value,
                                                                                                port_channel1_port3.value, port_channel1_port4.value,
                                                                                                port_channel1_port5.value, port_channel1_port6.value,
                                                                                                port_channel1_port7.value, port_channel1_port8.value)

port_channel2_announce = """Port-channel2 is configured with member interfaces: {} {} {} {} {} {} {} {}""".format(port_channel2_port1.value, port_channel2_port2.value,
                                                                                                port_channel2_port3.value, port_channel2_port4.value,
                                                                                                port_channel2_port5.value, port_channel2_port6.value,
                                                                                                port_channel2_port7.value, port_channel2_port8.value)

port_channel3_announce = """Port-channel3 is configured with member interfaces: {} {} {} {} {} {} {} {}""".format(port_channel3_port1.value, port_channel3_port2.value,
                                                                                                port_channel3_port3.value, port_channel3_port4.value,
                                                                                                port_channel3_port5.value, port_channel3_port6.value,
                                                                                                port_channel3_port7.value, port_channel3_port8.value)

port_channel4_announce = """Port-channel4 is configured with member interfaces: {} {} {} {} {} {} {} {}""".format(port_channel4_port1.value, port_channel4_port2.value,
                                                                                                port_channel4_port3.value, port_channel4_port4.value,
                                                                                                port_channel4_port5.value, port_channel4_port6.value,
                                                                                                port_channel4_port7.value, port_channel4_port8.value)

port_channel5_announce = """Port-channel5 is configured with member interfaces: {} {} {} {} {} {} {} {}""".format(port_channel5_port1.value, port_channel5_port2.value,
                                                                                                port_channel5_port3.value, port_channel5_port4.value,
                                                                                                port_channel5_port5.value, port_channel5_port6.value,
                                                                                                port_channel5_port7.value, port_channel5_port8.value)

port_channel6_announce = """Port-channel6 is configured with member interfaces: {} {} {} {} {} {} {} {}""".format(port_channel6_port1.value, port_channel6_port2.value,
                                                                                                port_channel6_port3.value, port_channel6_port4.value,
                                                                                                port_channel6_port5.value, port_channel6_port6.value,
                                                                                                port_channel6_port7.value, port_channel6_port8.value)




















if port_channel1_configured.value == 'Yes ':
    print(port_channel1_properties, file=open("FXOS_Config.txt", "a"))
else:
    print("Port-channel 1 not defined.")

if port_channel1_configured.value == 'Yes ':
    print(port_channel1_announce)

if port_channel1_port1.value == 'None':
    pass
else:
    print(portchannel1_1, file=open("FXOS_Config.txt", "a"))

if port_channel1_port2.value == 'None':
    pass
else:
    print(portchannel1_2, file=open("FXOS_Config.txt", "a"))

if port_channel1_port3.value == 'None':
    pass
else:
    print(portchannel1_3, file=open("FXOS_Config.txt", "a"))

if port_channel1_port4.value == 'None':
    pass
else:
    print(portchannel1_4, file=open("FXOS_Config.txt", "a"))

if port_channel1_port5.value == 'None':
    pass
else:
    print(portchannel1_5, file=open("FXOS_Config.txt", "a"))

if port_channel1_port6.value == 'None':
    pass
else:
    print(portchannel1_6, file=open("FXOS_Config.txt", "a"))

if port_channel1_port7.value == 'None':
    pass
else:
    print(portchannel1_7, file=open("FXOS_Config.txt", "a"))

if port_channel1_port8.value == 'None':
    pass
else:
    print(portchannel1_8, file=open("FXOS_Config.txt", "a"))

if port_channel1_configured.value == 'Yes ':
    print(portchannel_commit, file=open("FXOS_Config.txt", "a"))

if port_channel2_configured.value == 'Yes ':
    print(port_channel2_properties, file=open("FXOS_Config.txt", "a"))
else:
    print("Port-channel 2 not defined.")

if port_channel2_configured.value == 'Yes ':
    print(port_channel2_announce)

if port_channel2_port1.value == 'None':
    pass
else:
    print(portchannel2_1, file=open("FXOS_Config.txt", "a"))

if port_channel2_port2.value == 'None':
    pass
else:
    print(portchannel2_2, file=open("FXOS_Config.txt", "a"))

if port_channel2_port3.value == 'None':
    pass
else:
    print(portchannel2_3, file=open("FXOS_Config.txt", "a"))

if port_channel2_port4.value == 'None':
    pass
else:
    print(portchannel2_4, file=open("FXOS_Config.txt", "a"))

if port_channel2_port5.value == 'None':
    pass
else:
    print(portchannel2_5, file=open("FXOS_Config.txt", "a"))

if port_channel2_port6.value == 'None':
    pass
else:
    print(portchannel2_6, file=open("FXOS_Config.txt", "a"))

if port_channel2_port7.value == 'None':
    pass
else:
    print(portchannel2_7, file=open("FXOS_Config.txt", "a"))

if port_channel2_port8.value == 'None':
    pass
else:
    print(portchannel2_8, file=open("FXOS_Config.txt", "a"))

if port_channel2_configured.value == 'Yes ':
    print(portchannel_commit, file=open("FXOS_Config.txt", "a"))

if port_channel3_configured.value == 'Yes ':
    print(port_channel3_properties, file=open("FXOS_Config.txt", "a"))
else:
    print("Port-channel 3 not defined.")

if port_channel3_configured.value == 'Yes ':
    print(port_channel3_announce)

if port_channel3_port1.value == 'None':
    pass
else:
    print(portchannel3_1, file=open("FXOS_Config.txt", "a"))

if port_channel3_port2.value == 'None':
    pass
else:
    print(portchannel3_2, file=open("FXOS_Config.txt", "a"))

if port_channel3_port3.value == 'None':
    pass
else:
    print(portchannel3_3, file=open("FXOS_Config.txt", "a"))

if port_channel3_port4.value == 'None':
    pass
else:
    print(portchannel3_4, file=open("FXOS_Config.txt", "a"))

if port_channel3_port5.value == 'None':
    pass
else:
    print(portchannel3_5, file=open("FXOS_Config.txt", "a"))

if port_channel3_port6.value == 'None':
    pass
else:
    print(portchannel3_6, file=open("FXOS_Config.txt", "a"))

if port_channel3_port7.value == 'None':
    pass
else:
    print(portchannel3_7, file=open("FXOS_Config.txt", "a"))

if port_channel3_port8.value == 'None':
    pass
else:
    print(portchannel3_8, file=open("FXOS_Config.txt", "a"))

if port_channel3_configured.value == 'Yes ':
    print(portchannel_commit, file=open("FXOS_Config.txt", "a"))

if port_channel4_configured.value == 'Yes ':
    print(port_channel4_properties, file=open("FXOS_Config.txt", "a"))
else:
    print("Port-channel 4 not defined.")

if port_channel4_configured.value == 'Yes ':
    print(port_channel4_announce)

if port_channel4_port1.value == 'None':
    pass
else:
    print(portchannel4_1, file=open("FXOS_Config.txt", "a"))

if port_channel4_port2.value == 'None':
    pass
else:
    print(portchannel4_2, file=open("FXOS_Config.txt", "a"))

if port_channel4_port3.value == 'None':
    pass
else:
    print(portchannel4_3, file=open("FXOS_Config.txt", "a"))

if port_channel4_port4.value == 'None':
    pass
else:
    print(portchannel4_4, file=open("FXOS_Config.txt", "a"))

if port_channel4_port5.value == 'None':
    pass
else:
    print(portchannel4_5, file=open("FXOS_Config.txt", "a"))

if port_channel4_port6.value == 'None':
    pass
else:
    print(portchannel4_6, file=open("FXOS_Config.txt", "a"))

if port_channel4_port7.value == 'None':
    pass
else:
    print(portchannel4_7, file=open("FXOS_Config.txt", "a"))

if port_channel4_port8.value == 'None':
    pass
else:
    print(portchannel4_8, file=open("FXOS_Config.txt", "a"))

if port_channel4_configured.value == 'Yes ':
    print(portchannel_commit, file=open("FXOS_Config.txt", "a"))

if port_channel5_configured.value == 'Yes ':
    print(port_channel5_properties, file=open("FXOS_Config.txt", "a"))
else:
    print("Port-channel 5 not defined.")

if port_channel5_configured.value == 'Yes ':
    print(port_channel5_announce)

if port_channel5_port1.value == 'None':
    pass
else:
    print(portchannel5_1, file=open("FXOS_Config.txt", "a"))

if port_channel5_port2.value == 'None':
    pass
else:
    print(portchannel5_2, file=open("FXOS_Config.txt", "a"))

if port_channel5_port3.value == 'None':
    pass
else:
    print(portchannel5_3, file=open("FXOS_Config.txt", "a"))

if port_channel5_port4.value == 'None':
    pass
else:
    print(portchannel5_4, file=open("FXOS_Config.txt", "a"))

if port_channel5_port5.value == 'None':
    pass
else:
    print(portchannel5_5, file=open("FXOS_Config.txt", "a"))

if port_channel5_port6.value == 'None':
    pass
else:
    print(portchannel5_6, file=open("FXOS_Config.txt", "a"))

if port_channel5_port7.value == 'None':
    pass
else:
    print(portchannel5_7, file=open("FXOS_Config.txt", "a"))

if port_channel5_port8.value == 'None':
    pass
else:
    print(portchannel5_8, file=open("FXOS_Config.txt", "a"))

if port_channel5_configured.value == 'Yes ':
    print(portchannel_commit, file=open("FXOS_Config.txt", "a"))

if port_channel6_configured.value == 'Yes ':
    print(port_channel6_properties, file=open("FXOS_Config.txt", "a"))
else:
    print("Port-channel 6 not defined.")

if port_channel6_configured.value == 'Yes ':
    print(port_channel6_announce)

if port_channel6_port1.value == 'None':
    pass
else:
    print(portchannel6_1, file=open("FXOS_Config.txt", "a"))

if port_channel6_port2.value == 'None':
    pass
else:
    print(portchannel6_2, file=open("FXOS_Config.txt", "a"))

if port_channel6_port3.value == 'None':
    pass
else:
    print(portchannel6_3, file=open("FXOS_Config.txt", "a"))

if port_channel6_port4.value == 'None':
    pass
else:
    print(portchannel6_4, file=open("FXOS_Config.txt", "a"))

if port_channel6_port5.value == 'None':
    pass
else:
    print(portchannel6_5, file=open("FXOS_Config.txt", "a"))

if port_channel6_port6.value == 'None':
    pass
else:
    print(portchannel6_6, file=open("FXOS_Config.txt", "a"))

if port_channel6_port7.value == 'None':
    pass
else:
    print(portchannel6_7, file=open("FXOS_Config.txt", "a"))

if port_channel6_port8.value == 'None':
    pass
else:
    print(portchannel6_8, file=open("FXOS_Config.txt", "a"))

if port_channel6_configured.value == 'Yes ':
    print(portchannel_commit, file=open("FXOS_Config.txt", "a"))

print()

# Removes empty lines from config.
fh = open("FXOS_Config.txt", "r")
lines = fh.readlines()
fh.close()
keep = []
for line in lines:
    if not line.isspace():
        keep.append(line)
fh = open("FXOS_Config.txt", "w")
fh.write("".join(keep))
fh.close()

input('Configuration complete. Press enter key to exit')
