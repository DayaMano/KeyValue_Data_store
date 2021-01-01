from functions import *
import functions
import json
import threading


# the code will run repeated untill the user says otherwise
while True:
	print("Enter the following ")
	print("Enter - 1 to create new key")
	print("Enter - 2 to read the key")
	print("Enter - 3 to delete the key")
	print("Enter - 4 to save all the things")
	print("Enter - 5 to print the data")
	print("Enter - 6 to use the threads")
	print("Enter 'ctrl + c' to exit")
	#print("please ensure to save the other wise the data will be lost")

	operation = int(input())



	if operation == 1:
		print("Enter the Key : ")
		key = input()
		print("Enter the value : ")
		value = input()
		print("Do you wish for the key to have time-to-live : [y/n]")
		cond = input()

		# asking whether user wants to provide the key with time-to-live property or not
		if cond == 'y':
			print("Enter how long should the key be active (time in seconds) : ")
			time = int(input())
			functions.create(key, value, time)
		else:
			functions.create(key, value)
		functions.save()

	elif operation == 2:
		print("Enter the Key to read the value : ")
		key = input()
		print(functions.read(key))
		functions.save()

	elif operation == 3:
		print("Enter the Key to be deleted : ")
		key = input()
		functions.delete(key)
		functions.save()

	elif operation == 4:
		functions.save()
		

	elif operation == 5:
		functions.save()
		functions.printData()
		

	elif operation == 6:
		lock = threading.Lock()
		print("Enter the Key : ")
		key = input()
		t1 = threading.Thread(target = functions.delete(key,lock))
		t2 = threading.Thread(target = functions.delete(key,lock))
		t1.start()
		t2.start()
		t1.join()
		t2.join()
		functions.save()


	else:
		#condition = False
		print("error: please enter a valid operation")