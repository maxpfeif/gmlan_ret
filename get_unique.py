#	Authored: Max Pfeiffer - 2018
#
# 	Reads an input file in the Cabana.csv file format and produces an output file of just the unique CAN messages. 
#	The unique messages may include duplicate identifiers. 
#
# 	Software is free and open to anyone who wishes to use it under the GNU public license 
#
#	Usage: python get_unique.py "input_filename.csv" "bus"
#
#	Result:	unique_messages.csv in the working directory.
 
#!/usr/bin/python
import sys 
import csv

target_bus = sys.argv[2]
filename = sys.argv[1]

unique_id_msgs = []
unique_ids = []

# parse through the .csv file and check all the messages for duplicates 
def get_unique_messages(filename, target_bus):
	control = open(filename) 
	control_csv = csv.reader(control, delimiter = ",", quotechar = "|")
	header = 1 
	for row in control_csv:
		if header:
			header = 0
		else: 
			row.pop(0)	#throw away the timestamp, don't care 
			arb_id = row.pop(0)
			bus = row.pop(0)
			if bus == target_bus: 
				message = row.pop(0)
				entry = [arb_id, bus, message] 
				if entry not in unique_ids:
					unique_id_msgs.append(entry)
	control.close()
	return unique_id_msgs


# returns a list of the unique ids on the target bus 
def get_unique_ids(filename, target_bus):
	control = open(filename) 
	control_csv = csv.reader(control, delimiter = ",", quotechar = "|")
	header = 1 
	for row in control_csv:
		if header:
			header = 0
		else: 
			if(row.pop(2) == target_bus): 
				arb_id = row.pop(1)
				if arb_id not in unique_ids: 
					unique_ids.append(arb_id)
	control.close()
	return unique_ids


# saves a .csv file with all of the unique messages 
def save_unique_messages():
	new_log = open("unique_messages.csv", "w+")							
	new_writter = csv.writer(new_log, delimiter = ",")
	new_writter.writerow(["addr","bus","data"])  
	for row in unique_ids:
		new_writter.writerow(row)
	new_log.close()


# saves a .csv file with all of the unique ids, no message content 
def save_unique_ids():	
	new_log = open("unique_ids.csv", "w+")							
	new_writter = csv.writer(new_log, delimiter = ",")
	new_writter.writerow(["ID List"])  
	for row in unique_ids:
		new_writter.writerow(row)
	new_log.close()

