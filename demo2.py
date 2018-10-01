
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

	ofile  = open('converted.csv', "wb")
	writer = csv.writer(ofile, quotechar='"', quoting=csv.QUOTE_ALL)
 	
 	total_row = len(result)
 	
	for i in range(total_row):
		writer.writerow(result[i:(i+1)])

	ofile.close()



convert_ascii_to_ebcdic()