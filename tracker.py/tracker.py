 #tracker.py
#Author:Harshda Kumari
#Date: 2025-10-05
#Project:Daily Calorie Tracker

#Welcome message
print("Welcome to the Daily Calorie Tracker!")
print("This tool is made for tracking your daily calorie intake and compare your total with your daily limit." )
meal_names=[]
meal_calories=[]
num_meals=int(input("Enter the name of meal you want to enter today?"))
for i in range(num_meals):
    meal=input(f"Enter the name of meal {i+1}:")
    caloies=float(input(f"Enter calories for {meal}:"))
    meal_names.append(meal)
    meal_calories.append(calories)
    total_calories=sum(meal_calories)
    average_calories=total_calories/len(meal_calories)
    daily_limit =float(input("Enter your daily calorie limit:"))
if total_calories>daily_limit:
    print(f"You have exceeded your daily limit!)")
else:
    print(f"You are within your daily limit.")
#summary
print("Daily Calorie Summary")
print("Meal Name/Calories")

#For loop with f string formatting

for i in range((meal_names)):
    print(f"{meal_names[i]}  {meal_calories[i]}")
    print("-----------------------")
    print(f"Total Calories: {total_calories}")
    print(f"Average Calories per meal: {average_calories:.2f}")
    print(f"Dalily Calorie Limit: {daily_limit}")
    print("-----------------------")
    print("Thank you for using the Daily Calarie Tracker!")
    print("Stay healthy and mindful of your clorie intake!")






