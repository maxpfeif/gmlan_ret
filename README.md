# Python tools used to convert bus logs from Cabana to SavvyCAN formats   

Runing 
```
python get_diffs.py "control_filename.csv" "test_filename.csv"
```
creates two output files; new_log.csv and lost_log.csv 

new_log.csv contains messages exclusive to "test_filename.csv"  

lost_log.csv contains messages exclusive to "control_filename.csv

common messages to the two files are removed from both outputs 

# Converting Cabana Log Files to SavvyCAN Generic.csv Format 

```python savvy_convert.py "inputfile.csv" 1``` 

converts inputfile.csv saved from a Comma Ai Cabana log to the simple ID D0 D1 D2 D3 D4 D5 D6 D7 format SavvyCAN uses, with 1 being the bus of interest. It will produce a .csv with the savvy_ prefix added. 


# Converting Cabana Log Files to SavvyCAN GVRET.csv Format

```python gvret_convert.py "inputfile.csv" 1``` 

converts inputfile.csv saved from a Comma Ai Cabana log to the simple GVRET.csv format, with 1 being the bus of interest. It will produce a .csv with the gvret_ prefix added. 
