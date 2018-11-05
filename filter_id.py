#	Authored: Max Pfeiffer - 2018
#
#	Reads an input file in the Cabana.csv file format and takes a passed target ID to produce 
# 	an output file with only that ID in teh same Cabana format.  Note that the target ID must 
# 	be passed as an int 
# 
#	The output only sorts by ID, not message content. 
#
# 	Software is free and open to anyone who wishes to use it under the GNU public license 
#
#	Usage: python filter_id.py "input_filename.csv" "target ID"
#
#	Result:	"target ID"_messages.csv in the working directory. It also prints the averate period 
# 	between messages once the script has finished executing. 
 
#!/usr/bin/python
import sys 
import csv

filename = sys.argv[1]
target = sys.argv[2]

# parse through the .csv file and check all the messages for the targets 
def filter_id(filename, id_target, bus_target): 
	control = open(filename) 
	control_csv = csv.reader(control, delimiter = ",", quotechar = "|")
	
	header = 1 
	time_old = 0 
	time_new = 0
	avg_per = 0 
	counter = 0
	entry_list = []

	for row in control_csv:
		if header:
			header = 0	#throw away the header, don't care 
		else: 
			time = row.pop(0)  
			arb_id = row.pop(0)
			if arb_id == id_target: 
				bus = row.pop(0)
				if bus == bus_target:
					message = row.pop(0)
					entry = [time, arb_id, bus, message] 

					entry_list.append(entry)
					
					# update the periodic average, only look at positive time stamps 
					if(float(time) > 0):
						if(time_old == 0): 
							time_old = float(time)
						else: 
							time_new = float(time) 
							avg_per += time_new - time_old
							#print time_new - time_old
							time_old = time_new
							counter+= 1  
	control.close()

	# save the unique messages from the target id 
	new_log = open(id_target+"_messages.csv", "w+")							
	new_writter = csv.writer(new_log, delimiter = ",")
	new_writter.writerow(["time","addr","bus","data"])  
	for entry in entry_list:
		new_writter.writerow(entry)
	new_log.close()

	# return the average result 
	if(counter > 0):
		avg_result = float(avg_per)/counter
	else: 
		avg_result = 0
	return avg_result




