# GMLAN Reverse Engineering Tools used to decode CAN logs to identify messages of interest. 

These tools should allow an engineer recording CAN traffic using the Comma Ai Panda to do the following; 
1. Process Control and Test Logs, creating a diff output of the two 
2. Process Diff outputs for new messages relative to the control
3. Process Diff outpurs for missing messages relatie to the control 

The working directory with the gmlan_ret.py file should have two can logs in, control.csv and test.csv. 

Runing 
```
python gmlan_ret.py 
```
should create three output files in that directory; diff.csv, diff_new.csv and diff_old.csv 

The three files contain all, new and old bus traffic differences respectively. 
