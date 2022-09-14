#Question: Write a program that asks the user to enter the width and length of a room. Once these values have been read, your program should compute and display the area of the room. The length and the width will be entered as floating-point numbers. Include units in prompt and output message; either feet or meters, depending on which unit you are more confortable working with.
#Criteria: Exercise 3: Area of a Room (Solved, 13 Lines)

Unit = input("what unit would you want to use (Metric or Imperial): \n")
Width = input("Width of the room: \n")
Length = input("Length of the room: \n")

Metric_Area = float(Width) * float(Length)

Imperial_Area = float(Width) * float(Length)

if Unit == 'Metric':
    print('The area of the room in meters is: ' + str(Metric_Area) + 'm')

if Unit == 'Imperial':
    print('The area of the room in foot is: ' + str(Imperial_Area) + 'ft')