course_Name="Learn Python's Efficient Programming"
print("You are enrolled in Course: ",course_Name)

#Multi-line string value can be enclosed within '''
course_description='''This course is fully designed to fully equip
you with all you need to get started
with Python programming. Hope you Like it!!! '''

print("Your Course description is: ",course_description)

#String Operations:
print('Character present at index 4 is:',course_Name[4]) #returns 5th character of the string as Strings starts with Index: 0
print('Character present at index -1 is:',course_Name[-1]) #returns last character of the string
print("Characters in range 0: 4 of course_Name string is: ",course_Name[0:4]) # returns 0 to 3(4-1) index characters since end index(4) is excluded
print("Characters in substring for no end index is: ", course_Name[0:])#it will return all values till end of string if we dont mention end index value
print("Characers in substring for no start index is: ",course_Name[:5])#it will return 0 index till 4(5-1)
print("Cloning of a String:",course_Name[:]) #it will take all characters

#Formatted Strings
first_n = "Sri"
last_n = "N"
msg= f'{first_n} [{last_n}] is a coder'
print("message is: ",msg)