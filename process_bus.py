#	Authored: Max Pfeiffer - 2018
#
#	Reads log files in Cabana's .csv format and produces a .csv file with the 
# 	messages belonging to each unique id. Also produces a file containing the averating message period 
#	
#	Call: 	python process_bus.py "control.csv" "new.csv" "bus"
#			control.csv is the reference log file (i.e. quiescent, no changes)
#			new.csv is the variant log file 
# 			bus is the target bus we wish to analyze from the Cabana log 
#	
#	Result: 	a series of files "idx_messages.csv" for each unique ID in the log
# 				a periodic timing file, periods.csv, contianing the periods for each 
#				unique message ID logged into its own output file 
#
#	Dependencies: 	Requires that the get_diffs.py, get_unique.py and filter_id.py files 
# 					are in the PWD 
#
#	This software is free and open to anyone who wishes to use it

#!/usr/bin/python
import sys 
import csv
from get_diffs import * 
from get_unique import * 
from filter_id import * 

unique_arb_ids = []
bus_target = sys.argv[3]
id_periods = {}		# format = [id, time_old, time_new, avg_time, counter]

# generate a comprehensive list of the IDS in both files, as list_control and list_variant
populate_control_ids()
populate_variant_ids()

# now we want to generate the id lists for the specific output files 
detect_lost_ids()

# having generated these lists, lets create the three desired files 
save_lost_messages()

# get a list of the unique ids on the target bus 
unique_arb_ids = get_unique_ids("lost_log.csv", bus_target)

# call the filter_id.py methods for each unique ID, saving each output and populating the period list 
def filter_unique_id(filename, id_list, bus_target):
	for arb_id in id_list:
		id_periods[arb_id] = filter_id(filename, arb_id, bus_target)

# saves a .csv file withthe average periods 
def save_id_periods(id_periods): 
	avg_periods = open("average_periods.csv", "w+")
	period_writer = csv.writer(avg_periods, delimiter = ",")
	period_writer.writerow(["ID", "Average Period (Seconds)"])
	for arb_id in id_periods: 
		period_writer.writerow([arb_id, id_periods[arb_id]])
	avg_periods.close()

filter_unique_id("lost_log.csv", unique_arb_ids, bus_target)

save_id_periods(id_periods)









