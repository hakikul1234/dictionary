dictionary={'Hakikul':90,'Ramesh':85,'Alice':85,'Faizan':80,'kajal':90}

user_input=input("Enter the student's name:")

if user_input in dictionary:

     print(f"{user_input}'s marks:{dictionary[user_input]}")

else:
    print("Student not found.")