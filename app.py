# SU5_1
# nickname = input("Enter your nickname: ")
# hobby = input("Enter your hobby: ")
# print(f" your nickname is {nickname} and your hobby is {hobby}!")

# character = input("Enter a character: \n Steps")
# # predefined rows and columns
# rows = 6
# for i in range(rows):
#   for j in range(i):
#     print(character,end="")
# # creates a blank line between each column
#   print()



# SU_2
# allow the user to enter their age from the terminal and save it in a variable age
age = input("Enter your age: ")
# allow the user's friend to enter their age from the terminaland save it in a variable friend age
friend_age = input("Enter the age of your friend: ")
# concatenate the ages and print in terminal
print("Result: " + (age + friend_age))


# This is the sum values 
print("Sum values")
# allow the user to enter their age from the terminal and save it in a variable age and typecast it as int
age = int(input("Enter your age: "))
# allow the user's  friend to enter their age from the terminal and save it in a variable friend_age and typecast it as int
age = input("Enter your age: ")
friend_age = int(input("Enter the age of your friend: "))
result = age + friend_age
print("Result: " + str(result))
average_age = int(result)/2
print("Average age: " + str(average_age))