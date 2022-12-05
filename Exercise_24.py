#variables
secondsPerMin = 60
secondsPerHour = 3600
secondsPerDay = 86400
 
#user input
days    = int(input("Enter number of Days: "))
hours   = int(input("Enter number of Hours: "))
minutes = int(input("Enter number of Minutes: "))
seconds = int(input("Enter number of Seconds: "))
 
#Calculate the days, hours, minutes and seconds
total_seconds = days * secondsPerDay
total_seconds = total_seconds + ( hours * secondsPerHour)
total_seconds = total_seconds + ( minutes * secondsPerMin)
total_seconds = str(total_seconds + seconds)
 
#print answer
print("Total number of seconds: " + total_seconds)
