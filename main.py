#Leap Year Checker
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#If the year is divisible by 4
if year % 4 == 0:
  #If the year is divisible by 100
  if year % 100 == 0:
    #If the year is divisible by 400
    if year % 400 == 0:
      print("Leap Year")
    else:
      print("Not a leap year")
    #Year divisible by 4 but not 100 is leap
  else:
    print("Leap year")
else:
  print("Not a leap year")
