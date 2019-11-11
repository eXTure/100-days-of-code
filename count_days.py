#A script to count the days in the 100daysofcode log.
#The purpose of this script is to check if there's a correct number of days in the log file.

file_name = input('Enter log file name\n')
f = open(file_name, 'r', encoding='utf8')
number_of_days = 0
for line in f:
    if '2019' in line:
        number_of_days += 1
print(number_of_days)
f.close()
