original_list=[1,2,3,4,5,6,7,8,9,10]

data=original_list[0:5]
reverse_first=data.copy()
reverse_first.reverse()
print("Original list:",orginal_list)
print(f"Extracted first five elements:{data}")


print("Reversed Elements:",reverse_first)
