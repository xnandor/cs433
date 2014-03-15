#!/usr/bin/python

#################################################
##
## PAGE REPLACEMENT ALGORITHM PERFOMANCE
##
## by: Eric Bischoff
## for: UAB - CIS - cs433 - Spring 2014
##      Dr. Hyatt
##
## This Program is broken into 3 parts.
##     I. Reference String Generator
##    II. Page Replacement Simulator
##   III. Statistics Reporting
##
## The overall goal of this program is to
## arrive at an epiphany on the workings
## of common page replacement strategies;
## and to observe their behavior.
##

#IMPORTS
import random
import math
import enum from Enum

#SETTINGS
refStringLength = 10000
minPage = 0
maxPage = 100
meanPage = (maxPage-minPage)/2+minPage #mu in distibution - default is the midpoint between min and max page numbers.
stdPage = (maxPage-minPage)/6 #sigma in distribution - default is one sixth the distance from min to max page numbers.
workingSetSize = 5
e = 2.7182818285
pi = 3.1415926536

#INITIALIZATIONS
x = 0
refString = []
workingSet = []
pageFaults = 0
class Strategy(Enum): #Enum for Page Replacement Strategies
  random = 1
  mru = 2
  fifo = 3
  2xfifo = 4
  clock = 5
  nru = 6
  lru = 7
  optimal = 8
  nfu = 9
  aging = 10

#REFERENCE STRING GENERATOR
#get reference string from normal distribution of page numbers.
while (len(refString) < refStringLength):
  x = random.randint(minPage,maxPage)
  y = pow(e,-pow(x-meanPage,2)/(2*pow(stdPage,2)))/(stdPage*math.sqrt(2*pi))
  while (random.random() > y):
    x = random.randint(minPage,maxPage)
    y = pow(e,-pow(x-meanPage,2)/(2*pow(stdPage,2)))/(stdPage*math.sqrt(2*pi))
  if (len(refString) == 0): #duplicates don't matter when reference string is empty
    refString.append(x)
  elif (refString[len(refString)-1] != x): #don't allow duplicates
    refString.append(x)

#PAGE REPLACEMENT SIMULATOR


#STATISTICS REPORTING
print refString
