#!/usr/local/bin/python3

import xlrd
from xlrd.sheet import ctype_text

# the following functions (def xxx) are handlers for each of the rows of the XLS
# you need one of these for each of the 'things' that you're expecting to find in column A

def dns(myRV):
	# myRV is the 'local' copy of the list of cells that are passed into this function
	# it only exists while this function is being executed and doesn't exist outside of this fn
	print("scope system\n scope services\n  create dns %s\n" % myRV[1])
	return 1  # myRV no longer exists

def ntp(myRV):
	# this has its own myRV that, again, is local to this fn
	# it has the same name as the one above but they are different.
	print("scope system\n scope services\n  create ntp-server %s\n" % myRV[1])
	return 1

def interface(myRV):
	print("scope eth-uplink\n scope fabric a\n  enter interface %s" % myRV[1])  # interface ID, e.g. Ethernet1/1
	print("    %s" % myRV[2])		# enable/disable
	print("    set port-type %s" % myRV[3])
	print("    set auto-negotiation %s" % myRV[4])
	print("    set admin-speed %s" % myRV[5])
	print("    set admin-duplex %s" % myRV[6])
	return 1

def snmp(myRV):
	print("scope monitoring\n enable snmp\n  set snmp community\n  %s" % myRV[1])
	print("  set snmp syscontact %s" % myRV[2])
	return 1

def syslog(myRV):
	print("scope monitoring\n enable syslog remote-destination %s" % myRV[1])
	print("set syslog remote-destination %s level %s" % (myRV[1], myRV[2]))
	print("set syslog %s hostname %s" % (myRV[1], myRV[3]))
	print("set syslog remote-destination %s facility %s" % (myRV[1], myRV[4]))
	return 1

# this funky little thing maps whatever you find in column A to the functions above
# (the names match at the moment but they don't have to)
dynDispatch = {
	'dns': dns,
	'ntp': ntp,
	'interface': interface,
	'snmp': snmp,
	'syslog': syslog
}

################
##### MAIN #####
################

# open the workbook and call it wb TODO: make this a CLI parameter
wb = xlrd.open_workbook('excel_inputs.xlsx')

# take each sheet of the wb and iterate through that...
for i, ws in enumerate(wb.sheets()):
	# output a fancy(ish) header/marker
	print("\n###############################\n   Chassis: %s \n###############################" % ws.name)
	
	# take each row in the sheet. nrows means that we only go through the number of rows that are actually used
	# TODO print a warning if nrows is large, just in case we've got a pile of rubbish in there
	for r in range(ws.nrows)[0:]:
		# grab the row and stick all its cells in an array called rv
		rv = ws.row_values(r)
		# put the contents of the first cell of this row into a variable 'callThis' and make it lower case
		callThis = rv[0].lower()
		# test to see if we have a subroutine for this row..
		if callThis in dynDispatch:
			# ...and call that subroutine and give it the other cells of that row to play with
			dynDispatch[callThis](rv)
			# anything that fails this test is silently ignored.
			# which is useful
			# and intentional!
			# and means you can have comments in the XLS ;)

