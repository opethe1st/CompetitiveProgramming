#!/bin/python

import sys

monthdays = [31,28,31,30,31,30,31,31,30,31,30,31]
year = int(raw_input().strip())
# your code goes here


if year!=1918:
    if (year<1918 and year%4==0) or (year>1918 and (year%400==0 or (year%4==0 and year%100!=0))):
        #leap year
        monthdays[1]+=1

    daysleft = 256
    month = 0
    while daysleft>0:
        daysleft-=monthdays[month]
        #print daysleft
        month+=1

    daysleft+=monthdays[month-1]
    print '%02d.%02d.%4d'%(daysleft,month,year)
else:
    monthdays[1]= 15

    daysleft = 256
    month = 0
    while daysleft>0:
        daysleft-=monthdays[month]
        #print daysleft
        month+=1

    daysleft+=monthdays[month-1]
    print '%02d.%02d.%4d'%(daysleft,month,year)
