# GREP, AWK, SED

All these are command line utilities to perform various text processing functions.

Note - You need to have this file [studentData.lst](https://github.com/AbhigyanBafna/brain2/blob/main/OS/studentData.lst) for running these commands.

## Global Regular Expression Print (GREP)

```
#Displays Borivali people
grep Borivali studentData.lst

#New list for Thane people
grep Thane studentData.lst>Thane.lst
```

## AWK

```
#Displays name surname marks
awk '{print $3 "\t" $4 "\t" $9}' studentData.lst

#Creates a new file for people with 85% and above %
awk '$9>85' studentData.lst > distinction.lst
```

## Stream Editor (SED)

```
#Displays all content in file
sed -n 'p' studentData.lst

#Displays line 4-8
sed -n '4,8p' studentData.lst
 
#Displays top 4 lines
sed '4q' studentData.lst

#Filters Byculla people to a new list
sed -n '/Byculla/p' studentData.lst > byculla.lst
```