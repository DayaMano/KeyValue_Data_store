import json
import threading
from threading import *
import time
import sys
import optionalFilePath

# all the data are stored in json file for presistant storage
# since data is stored as key-value pair in json
path = optionalFilePath.getDataFile()
path.replace('\\\\','\\')
#print(path)
file = open(path)
data = json.load(file) # the data is than transfered to a dict
file.close()
#print('no error')


def create(key, value, timeout=0):
	# prints error massage if the key is not in the database
	if key in data.keys():
		print("error: the key is already present.")
	else:
		# checking whether the key is a string 
		if(key.isalpha()):
			# to check whether the data is within 1GB (1073741824 in bytes) and the value is within 16Kb
			# sys.getsizeof() method will return size of dict in bytes 
			if sys.getsizeof(data) < 1073741824 and sys.getsizeof(value) <= (16 * 1024):
				if timeout == 0:
					pair = [value, timeout]
				else:
					pair = [value, time.time() + timeout]
				# checking whether the key is within the limit of 32 characters
				if len(key) <= 32:
					data[key] = pair
			else:
				print("error: Memory limit exceeded")
		else:
			print("error: Invalid key. the key must only contain alphabets")

def read(key,lock):
	# returns error message if the key is not present in the data
	lock.acquire()
	if key not in data.keys():
		lock.release()
		return "error: the key does not exists in the database."
	else:
		valuePair = data[key]
		if valuePair[1] != 0:
			# checking whether the key within the time-to-live property
			# if the key has exceeded the time-to-live period the key will be deleted
			if time.time() < valuePair[1]:
				lock.release()
				return dict({ "key" : "data[key][0]" })
			else:
				lock.release()
				del data[key]
				return str("error: time-to-live of the provided key {0} has expired".format(key))
		else:
			lock.release()
			return dict({ key : data[key][0] })


def delete(key,lock):
	# checks whether the key is in the database or not
	lock.acquire()
	if key not in data.keys():
		lock.release()
		print("error: the key does not exists in the database.")
	else:
		valuePair = data[key]
		if valuePair[1] != 0: # checking whether the key is still alive or not
			if time.time() < valuePair[1]:
				lock.release()
				del data[key]
			else:
				lock.release()
				del data[key]
				print("error: time-to-live of the provided key {} has expired and the key has been deleted from the database".format(key))
		else: # if the key does not have time-to-live property
			lock.release()
			del data[key]
			print("Key deleted successfully")
			return

def save():
	# this function will write all the data in the dictionary into json file for presistant storage
	with open(path,'w') as jsonFile:
		json.dump(data, jsonFile)

def printData():
	# checking whether dict is empty or not
	if len(data) == 0:
		print('There is no data in the database')
	else: #if the dict is not empty it will print the data in key : value pair
		# for key, value in data.items():
		# 	print("{0} : {1}".format(key, value))
		with open(path,'w') as jsonFile:
			json.dump(data, jsonFile)
		with open(path, 'w') as jsonFile:
			string = json.dumps(data, indent=4)
		print(string)	
