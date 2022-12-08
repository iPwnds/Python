#user input
userInput = input("insert month: ")
#arrays for months with 30 and 31 days
monthsWith31 = ["january", "march", "may", "july", "august", "october", "december"]
monthsWith30 = ["april", "june", "september", "november"]
#if function
if userInput in monthsWith31:
    print("there are 31 days in this month")
elif userInput == "february":
    print("there are 28 days in this month")   
elif userInput in monthsWith30:
    print("there are 30 days in this month")
else:
    print("insert valid month")
