#!/usr/bin/env python3

# Advent day 1
import numpy

hand = open('input.txt')

count = 0
allist = list()
totnumber = 0

for line in hand :
	line = line.rstrip()
	if len(line) != 0 :
		totnumber = totnumber + int(line)
	else :
		print('totnumber of elf ', count + 1, 'equals', totnumber)
		allist.append(totnumber)
		totnumber = 0
		count = count + 1

print('totnumber of elf ', count + 1, 'equals', totnumber)
allist.append(totnumber)

print(max(allist))

a = max(allist)
b = 0

for i in range(3) :
	print(a)
	b = b + a
	allist.remove(a)
	a = max(allist)
print(b)
