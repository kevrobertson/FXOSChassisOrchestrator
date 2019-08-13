# Imports all the defined strings from excel document
from excel_strings2 import *



ethernet11 = [ethernet11_int.value, ethernet11_enable.value,
          ethernet11_type.value, ethernet11_autoneg.value,
          ethernet11_speed.value, ethernet11_duplex.value]
for x in ethernet11:
  print(x)

