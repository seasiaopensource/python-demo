
"""
Convert 'ASCII' to EBCDIC package.
"""

import ebcdic
import csv

def convert_ascii_to_ebcdic():
	#Reading csv file
	result = []
	with open('example.csv', 'rb') as readFile:
		reader = csv.DictReader(readFile)
		for row in reader:
			result.append(row['Title'].encode('cp1140'))
			
	print result

 
convert_ascii_to_ebcdic()