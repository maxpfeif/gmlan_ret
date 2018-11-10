#	Authored: Max Pfeiffer - 2018
#
#	Converts the .csv file from Saleae logic to a usable Cabana can data file for processing data in Cabana
# 	or for using one of the existing decode formats. Note that this drops all ACK, CRC and RTR information. 
#
#	Usage: 	python convert_saleae.py "saleae_logfile.csv" "bus"
#		"saleae_logfile.csv" = the file to decode 
#		"bus"	= a user defined label for the bus we're analyzing 
#
#	Output: cabana_saleae_logfile.csv in the proper format 
#
#!/usr/bin/python
import sys 
import csv
from decimal import *


#keeps track of the header 
header = 1 


# message contents
time = 0 
can_id = 0 
data = "" 


# open the input file 
input_file = open(sys.argv[1]) 
og_data = csv.reader(input_file, delimiter = ",", quotechar = "|")


# make a new file as the output file 
output_data = open("cabana_"+ sys.argv[1], "w+")							
output_writer = csv.writer(output_data, delimiter = ",")
output_writer.writerow(["Time Stamp", "ID", "Bus", "Data"]) 


# returns true if passed a CAN ID row 
def is_header(in_list):
	# need to first check if the length of the list is at least 12 
	if len(in_list) > 12:
		if ord(in_list.pop(9)) == 67: 
			return 1 
	return 0  


# returns true if passed a data row  
def is_data(in_list): 
	# the first value in the list is always a 'D' if its a data byte 
	check_first = in_list.pop(0)
	if(ord(check_first) == 68):
		return 1   
	return 0 


# returns the hex data portion of the passed list as a list 
def extract_hex(in_list):
	# find the first open paren 
	cur_char = ord(in_list.pop(0))
	while (cur_char != 40):
		cur_char = ord(in_list.pop(0))
	
	# extract the hex contents until the close paren 
	new_list = []
	next_element = in_list.pop(0)
	while (cur_char != 41):
		new_list.append(next_element)
		next_element = in_list.pop(0)
		cur_char = ord(next_element)

	# return the result in string form 
	result = ""
	while(len(new_list)):
		result = result + str(new_list.pop(0)) 
	return result


# saves the present message content 
# resets the message content variables
def save_message(): 
	output_writer.writerow([time, can_id, sys.argv[2], data])
	time = 0 
	data = "" 


# iterate over all of the rows, checking for the CAN ids and data 
for row in og_data:
	if header:
		header = 0
	else:
		# record the time field  
		time = row.pop(0)
		# get the row contents as a list 
		row_data = list(row.pop(1))
	
		if(is_header(row_data)):
			if(can_id > 0): # if we're not in the initial case where the can_id = 0 
				save_message()
				data = ""
			can_id = extract_hex(row_data)

		elif(is_data(row_data)): 
			hex_data = list(extract_hex(row_data))
			data = data + hex_data.pop(2) 
			data = data + hex_data.pop(2)


