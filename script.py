#! /usr/bin/env/python3


#make sure to run the bash script to create the info.txt and error.txt before hand
import re

error_path = '{PATH TO THE ERROR.TXT FILE CREATED BY THE BASH SCRIPT}'
info_path = '{PATH TO THE INFO.TXT FILE CREATED BY THE BASH SCRIPT}'
error_dictionary = {}       # empty dictionary for error count based on error message
user_error_dictionary = {}  # empty dictionary for the error count based on users
user_info_dictionary = {}   # empty dictionary for info count based on users
info_pattern = r'(INFO).(\w\w.+) (\[.+\]) \((\w.+)\)'
error_pattern = r'(ERROR).(\w\w.+) \((\w.+)\)'

def create_error_dictionary(): 
    with open(error_path,'r') as info: # open the file that has the error portions of the system logs
        line = info.readlines()
        for lines in line:
            message=re.search(error_pattern,lines)
            type,error_info,user = message.groups() #assigns the values of the regex group to the right variables
            
            if error_info not in error_dictionary: #if-else statement that checks if the error message is already in the dictionary
                error_dictionary[error_info] = 1 # if message not already in the dictionary, creates the entry with a value of one
            else:
                error_dictionary[error_info] += 1 # if message is in the dictionary, it adds one to the count

def create_user_error_dictionary():
    with open(error_path,'r') as info: #opens the error portion of the system logs
        line = info.readlines()
        for lines in line:
            message=re.search(error_pattern,lines)
            type,error_info,user = message.groups() #assigns the values based on the regex group
            
            if user not in user_error_dictionary: # if-else statement to check user is already in the dictionary
                user_error_dictionary[user] = 1   # if user not in the dictionary, create the entry with an itital value of one
            else:
                user_error_dictionary[user] += 1  # if user is in the dictionary, add one to the count


def create_user_info_dictionary():
    with open(info_path,'r') as info: #opens the info portion of the system logs
        line = info.readlines()
        for lines in line:
            message=re.search(info_pattern,lines)
            type,error_info,ticket,user = message.groups() # assigns values based on regex groups
            
            if user not in user_info_dictionary: # if-else statement to check if user is in dictionary
                user_info_dictionary[user] = 1  # if user not in dictionary, create entry with intial value of one
            else:
                user_info_dictionary[user] += 1 # if user already in the dictionaty, add one to the count

def create_user_csv(): # creates a a csv_file with the user name, info count based on the user and the error count based on user
    with open("user_data.csv","w") as file: # creates the file and names it user_data.csv
        file.writelines('username,info,error\n') # creates a header for the CSV
        
        for i in user_info_dictionary.keys():
            file.writelines(i + ',' + str(user_info_dictionary[i])+ ',' + str(user_error_dictionary[i]) + '\n') # creates entries :username,info_count,error-count

def create_error_csv(): # creates a CSV file based on the error message and the count of the error messages
    with open("error_data.csv","w") as file:
        file.writelines('messsage,count\n')# creates a header for the CSv file

        for i in error_dictionary.keys():
            file.writelines(i + ',' + str(error_dictionary[i])+'\n') # creates a entries: error_message,error_count
                            





#run all the functions created above
create_error_dictionary()
create_user_error_dictionary()
create_user_info_dictionary()
create_user_csv()
create_error_csv()










    
