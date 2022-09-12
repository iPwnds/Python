Unit = input("what unit would you want to use (Metric or Imperial): \n")
Width = input("Width of the room: \n")
Length = input("Length of the room: \n")

Metric_Area = float(Width) * float(Length)

Imperial_Area = float(Width) * float(Length)

if Unit == 'Metric':
    print('The area of the room in meters is: ' + str(Metric_Area) + 'm')

if Unit == 'Imperial':
    print('The area of the room in foot is: ' + str(Imperial_Area) + 'ft')