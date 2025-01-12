list = ["Bob","Alice","Ram"]
tuple = ("Bob","Alice","Ram")
set = {"Bob","Alice","Ram"}

# Can't add or remove things from tuple
# List has difference, union, intersection methods

DaysInWeek = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}
WorkoutDays = {"Monday", "Tuesday", "Wednesday", "Friday", "Saturday"}
RestDays = {"Sunday", "Thursday"}
MealPrepDays = {"Sunday", "Tuesday", "Friday"}

inputDay = input("Enter the day : ")

if(inputDay in WorkoutDays):
    print("It was workout day on {}".format({inputDay}))
if(inputDay in RestDays):
    print("It was rest day on {}".format(inputDay))
if(inputDay in MealPrepDays):
    print("It was mealprep day on {}".format(inputDay))
if(inputDay not in DaysInWeek):
    print("{} in a invalid day".format(inputDay))
