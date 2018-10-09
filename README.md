# GMLAN Reverse Engineering Tools used to process bus logs from Cabana in SavvyCAN and Python 

CAN traffic recorded using Panda can be used witht these tools to.. 
2. Process Diff outputs for new messages relative to the control
3. Process Diff outpurs for missing messages relatie to the control 

Runing 
```
python gmlan_ret.py "control_filename.csv" "test_filename.csv"
```
should create three output files in that directory; filename_new.csv and filename_lost.csv 

The three files contain all, new and old bus traffic differences respectively. 

# Converting Cabana Log Files to SavvyCAN Generic.csv Format 

```python savvy_convert.py "inputfile.csv" 1``` 

converts inputfile.csv saved from a Comma Ai Cabana log to the simple ID D0 D1 D2 D3 D4 D5 D6 D7 format SavvyCAN uses, with 1 being the bus of interest. It will produce a .csv with the savvy_ prefix added. 


# Converting Cabana Log Files to SavvyCAN GVRET.csv Format

```python gvret_convert.py "inputfile.csv" 1``` 

converts inputfile.csv saved from a Comma Ai Cabana log to the simple GVRET.csv format, with 1 being the bus of interest. It will produce a .csv with the gvret_ prefix added. 
