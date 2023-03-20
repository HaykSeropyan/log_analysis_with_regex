# log_analysis_with_regex
This is based on the week 7 lab of the "Using Python to interact with the Operating System Module"


This is a collection of scripts for the final lab of the "Using Python to interact with the Operating System" module.
The bash script converts the log file into to seperate text files based on the type of error message( INFO and ERROR ) called info.txt and error.txt

after that the python script (script.py) uses the two text files to create three dictionaries: error_count, user_error_count and user_info_count. Using these dictionaries it makes a unsorted csv files that can be used with the csv_to_html.py script to make it into a webpage.

**REMEBER TO CHANGE THE PATH VARIABLES IN THE SCRIPT.PY TO THE RIGHT PATH FOR THE SCRIPT NOT TO THROUGH AN ERROR***

since the csv file will not be sorted, the script will be needed to be modified to pass all the requirments of the lab.
