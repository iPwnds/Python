#Question: An online retailer sells two products: widgets and gizmos. Each widget weighs 75 grams. Each gizmo weighs 112 grams. Write a program that reads the number of widgets and the number of gizmos from the user. Then your program should compute and display the total weight of the parts.
#Criteria: Exercise 8: Widgets and Gizmos (15 Lines)

widgetWeight = 75

gizmoWeight = 112

widgetAmount = input('How many widgets do you own: \n')

gizmoAmount = input('How many gizmos do you own: \n')

totalWidget = int(widgetWeight) * int(widgetAmount)

totalGizmo = int(gizmoWeight) * int(gizmoAmount)

Total = int(totalWidget) + int(totalGizmo)

print('Your Widgets weigh: ' + str(totalWidget) + ', and Your Gizmos weigh: ' + str(totalGizmo) + ', Which is a total weight of: ' + str(Total))