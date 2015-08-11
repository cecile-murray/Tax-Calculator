import sys
import json
import csv

#============================================================================================================#
# Useful Functions
# Author: Cecile Murray, cecile.murray@gmail.com
# Date: August 2015
# 
# THIS VERSION IS FOR MS WINDOWS ONLY.
#
# This file contains a handful of small functions that make working with Python dictionaries and serializing them
# in JSON substantially easier. 
#
# DEPENDENCIES: none
#
#============================================================================================================#


# Serializes file into JSON
def dump_to_file(dictionary, filename):
    f = open(filename, 'w')
    json.dump(dictionary, f, indent=2, separators=(',', ':'))
    f.close()
    return

# Reads json file back into usable form
def read_json_file(filename):
	f = open(filename, 'r')
	data = json.load(f)
	f.close()
	return data

# Print a dictionary
def print_dict(dictionary):
    for d in dictionary:
    	print d
        print dictionary[d]
    return

# Reads csv file into a list
def csv_to_list(filename):
    data = []
    with open(filename, 'rU') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for r in reader: 
            data.append(r)
    return data

# Write a JSON file to .csv 
# 1. get the data out of JSON
# 2. open the csv you're going to write it to
# 3. iterate through the dictionary: each line is tract id, total jobs, jobs in sector

def convert_json_to_csv(json_file, l, csv_file):
	tracts = read_json_file(json_file)
	with open(csv_file, 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=l)
		writer.writeheader()
	return

# Takes dict and returns list of keys, sorted
def make_dict_to_list(dictionary):
	rv = []
	for key in dictionary:
		rv.append(key)
	rv.sort()
	return rv

def write_nested_list(nested_list, filename):
	with open(filename, 'wb') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')
		for l in nested_list:
			writer.writerow(l)
	return

def check_sector_count(dictionary):
	for d in dictionary:
		nest = dictionary[d]['jobs']['sector']
		length = len(nest)
		print length
		#if length != 20:
			#print 
			#return False
	return True

# Courtesy of AMR and CS122, PA#1
def read_request(request): 
    '''
    Return data from request object.  Returns result or "" if the read
    fails.
    '''

    try:
        return request.text.encode('iso-8859-1')
    except:
        print "read failed: " + request.url
        return ""

# Makes all scrapes uniform, of identifier home, work(?)
def clean_travel_data(filename, file_num):
    rv = []
    data = read_json_file(filename)
    for d in data:
        line = d[0].split('-')
        if file_num < 97:    
            temp = line[2] + '-' + line[1]
        else:
            temp = line[1] + '-' + line[2]
        rv.append([temp, d[1], d[2]])

    return rv


