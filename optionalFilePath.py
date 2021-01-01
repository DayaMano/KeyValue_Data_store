import json
import os
from pathlib import Path

def getDataFile():
	print("Enter the json file name : ")
	fileName = str(input())
	if '.json' not in fileName:
		fileName = fileName + '.json'
	print("Enter the path to create the json file : ")
	filePath = str(input())

	

	if not os.path.exists(filePath):
		print("error: the path entered does not exist")
		# if the entered path is not correct than the data file will be
		# created in the default source code file folder
		if os.path.isfile(fileName):
			return os.path.abspath(fileName)
		else:
			fhand = open(fileName, 'a')
			fhand.write("{ }")
			fhand.close()
			print(str(os.path.abspath(fileName)))
			return str(os.path.abspath(fileName))
	else:
		filePath = os.path.join(filePath, fileName)
		print('no error')
		#path = os.path.join(filePath, fileName)
		# if the json data already exists 
		# than we just need to return the path for that particular file
		myFile = Path(filePath)
		#os.path.isfile(filePath)
		if myFile.is_file():
			#print('file exist')
			return os.path.abspath(filePath)
		# if the does not exist
		# than we need to creat that json file in that folder and return the path for that file
		else:
			#print('new created')
			fhand = open(filePath, 'a')
			fhand.write("{ }")
			fhand.close()
			return str(filePath)
		