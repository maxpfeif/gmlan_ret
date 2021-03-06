#	Authored: Max Pfeiffer - 2018
#
#	Reads the .csv file format generated by Comma Ai's Cabana and converts to
#	the GVRET format supported for use with Collin Kidder's SavvyCAN 
#
#	Preconditions: 	sourcefilename.csv 
#					Bus ID of interest (i.e. "1") 
#	
#	Outputs:		gvret_sourcefilename.csv 
#					
#	Example: $ python gvret_convert.py cabana_output.csv 1

# ------- Desired Output Format -------- 
# Time Stamp,ID,Extended,Bus,LEN,D1,D2,D3,D4,D5,D6,D7,D8
# 166064000,0000021A,false,0,6,00,C0,F4,41,96,A2,00,00,

# ------- TODO - CHECK WHY THE HEX FORMAT IS NOT BEING READ PROPERLY, need to put the plug bits at the END, this is an endian issue 

#!/usr/bin/python
import sys 
import csv
from decimal import *

header = 1

with open(sys.argv[1]) as original:
	og_data = csv.reader(original, delimiter = ",", quotechar = "|")
	# make a new file as the output file 
	gvret_data = open("gvret_"+sys.argv[1], "w+")							
	gvret_writer = csv.writer(gvret_data, delimiter = ",")
	gvret_writer.writerow(["Time Stamp", "ID", "Extended", "Bus", "LEN", "D1" , "D2", "D3", "D4", "D5", "D6", "D7", "D8"])  
	
	for row in og_data:
		if header:
			header = 0
		else: 
			if(row.pop(2) == sys.argv[2]):
				# get the message time from the input file -- convert to micros 
				msg_time = long(1000000 * float(row.pop(0)))

				# get the data from the input file
				msg_data = list(row.pop(1))

				# need to calculate the length of this data and save that parameter to the data_len
				# check odd-value case 
				if len(msg_data) % 2 > 0:
					msg_data.insert(0,"0")					
				data_len = len(msg_data)/2

				# need to concatenate every two bytes	
				for i in range(0,data_len):
					# pop the two bytes off of the data, or two entries from the list and concatenate them, then add them back to the end of the list 
					b0 = msg_data.pop()	
					# handle the case where the the msg_data is empty.. 
					if len(msg_data) < 1: 
						b1 = "0"
					else:	
						b1 = msg_data.pop()
					concat = b1 + b0
					msg_data.insert(0,concat.upper())

				# stuff the remaining space 
				while len(msg_data) < 8:
					msg_data.append("00")

				# converts the address format and checks for extended ID
				addr = int(row.pop(0))
				extended = addr > 4095
				addr = str(hex(addr))
				addr =list(addr)
				addr.remove("x")
				while len(addr) < 8:
					addr.insert(0,0) 
				str_addr = ""
				while len(addr) > 0:
					str_addr = str(addr.pop()) + str_addr
				addr = str_addr.upper()

				# need to write time, ID, extended, bus, len, then all of the data bytes.
				msg_data.insert(0, data_len)
				msg_data.insert(0, sys.argv[2])
				if extended:
					msg_data.insert(0,"true")
				else: 
					msg_data.insert(0,"false")
				msg_data.insert(0,addr)
				msg_data.insert(0,msg_time)
				gvret_writer.writerow(msg_data)


gvret_data.close()
original.close()


