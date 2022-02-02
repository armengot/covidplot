#!/usr/bin/python3
import csv
import sys
import wget
import numpy as np
import matplotlib.pyplot as plt
import datetime

normal="\033[0m";
redbold="\033[1m\033[1;31m";
blubold="\033[1m\033[1;34m";

license ="\n\t"+blubold+"covidplot.py"+normal+" to single plot from COVID19 stats\n"
license+="\tCopyright (C) 2022 Marcelo Armengot @armengotmarcelo\n\n"
license+="\tThis program is free software: you can redistribute it and/or modify\n"
license+="\tit under the terms of the GNU General Public License as published by\n"
license+="\tthe Free Software Foundation, either version 3 of the License, or\n"
license+="\t(at your option) any later version.\n\n"
license+="\tThis program is distributed in the hope that it will be useful,\n"
license+="\tbut WITHOUT ANY WARRANTY; without even the implied warranty of\n"
license+="\tMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n"
license+="\tGNU General Public License for more details.\n\n"
license+="\tYou should have received a copy of the GNU General Public License\n"
license+="\talong with this program.  If not, see https://www.gnu.org/licenses/gpl-3.0.html.\n"

def samequarter(str1,str2):
    d1 = int(str1.split('-')[2])
    d2 = int(str2.split('-')[2])    
    m1 = int(str1.split('-')[1])
    m2 = int(str2.split('-')[1])
    y1 = int(str1.split('-')[0])
    y2 = int(str2.split('-')[0])
    if (y1==y2)and(m1==m2):
        if d1<16:
            q1 = 1
        else:
            q1 = 2
        if d2<16:
            q2 = 1
        else:
            q2 = 2
        if q1==q2:
            return(True)
        else:
            return(False)
    else:
        return(False)

def samemonth(str1,str2):
    m1 = int(str1.split('-')[1])
    m2 = int(str2.split('-')[1])
    y1 = int(str1.split('-')[0])
    y2 = int(str2.split('-')[0])
    if (y1==y2)and(m1==m2):
        return(True)
    else:
        return(False)

country = sys.argv[1]
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
try:
    print("Looking for data in "+url)
    wget.download(url)
except:
    print("Connection fail.")
    exit(0)

file = url.split('/')[-1]
with open(file,'r') as f:
    for line in f.readlines():
        header = line.split(',')
        break
f.close()
idate = header.index('date')
inews = header.index('new_cases')
idths = header.index('new_deaths')
ipops = header.index('population')
ilocs = header.index('location')
print(license)
print("Showing plot of: "+blubold+header[idate]+' '+header[inews]+' '+header[idths]+normal)
print("Data from: "+redbold+country+normal)
print("Source: "+url.split('/')[2])
data = []
with open(file,'r') as f:
    for line in f.readlines():
        row = line.split(',')
        if (row[ilocs]==country):
            data.append([row[idate],row[inews],row[idths],row[ipops]])
f.close()
time = np.zeros(50,dtype='datetime64[D]')
news = np.zeros(50,dtype='float')
dths = np.zeros(50,dtype='float')
pops = np.zeros(50,dtype='float')
i = 0
current_month = data[0][0]
print(current_month)
tt_cases = 0
tt_death = 0

j = 0
for item in data:   
    j = j + 1
    time[i] = np.datetime64(current_month)
    pops[i] = float(item[3])
    if samequarter(item[0],current_month):  # could switch to samemonth()
        if item[1]!='':
            tt_cases = tt_cases + abs(float(item[1]))        
        if item[2]!='':
            tt_death = tt_death + abs(float(item[2]))
    else:        
        current_month = item[0]            
        news[i] = tt_cases #/pops[i]
        dths[i] = tt_death #/pops[i]
        if item[1]!='':
            tt_cases = abs(float(item[1]))
        else:
            tt_cases = 0
        if item[2]!='':
            tt_death = abs(float(item[2]))
        else:
            tt_death = 0
        i = i + 1

    if news[i]<0:
        news[i]=0        
        print("Cases number<0?  : "+str(item))
    if dths[i]<0:
        dths[i]=0
        print("Deaths number<0? : "+str(item))
    

_,tv1 = plt.subplots()
tv1.bar(time,news,color='b',width=11,align='edge')
tv1.grid(color='tab:gray', linestyle=':', linewidth=1)
tv1.set_title("COVID19: "+country+" (cases)")
tv1.set_xlim(np.datetime64("2020-02-20"),np.datetime64("today"))
tv1.set_xlabel("Source:\n"+url)
tv1.get_yaxis().get_major_formatter().set_scientific(False)
plt.pause(0.1)
_,tv2 = plt.subplots()
tv2.bar(time,dths,color='r',width=11,align='edge')
tv2.grid(color='tab:gray', linestyle=':', linewidth=1)
tv2.set_title("COVID19: "+country+" (deaths)")
tv2.set_xlim(np.datetime64("2020-02-20"),np.datetime64("today"))
tv2.set_xlabel("Source:\n"+url)
tv2.get_yaxis().get_major_formatter().set_scientific(False)
plt.show()
