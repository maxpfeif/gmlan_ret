# GMLAN Reverse Engineering Tools used to decode CAN logs to identify messages of interest. 

CAN traffic recorded using Panda can be used witht these tools to.. 
1. Process Control and Test Logs, creating a diff output of the two 
2. Process Diff outputs for new messages relative to the control
3. Process Diff outpurs for missing messages relatie to the control 

Runing 
```
python gmlan_ret.py "control_filename.csv" "test_filename.csv"
```
should create three output files in that directory; filename_diff.csv, filename_new.csv and filename_lost.csv 

The three files contain all, new and old bus traffic differences respectively. 

# Converting CabanaLog Files for SavvyCAN 

```python savvy_convert.py "inputfile.csv" 1``` 

allows you to convert inputfile.csv saved from a Comma Ai Cabana log to the simple ID D0 D1 D2 D3 D4 D5 D6 D7 format SavvyCAN uses, with 1 being the bus of interest. It will produce a .csv with the savvy_ prefix added. 

