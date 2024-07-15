number = {2, 3, 5, 7, 11}
print("First five prime numbers: ", number)

number.add(11)
print("\nAdd the number 11 to the set: ", number)


number.remove(2)
print("\nRemove the number 2 from set: ", number)

is_seven_in_set = 7 in number
print("\nCheck if the number 7 is in the set: ", is_seven_in_set) 

print("\n The Final set: ",number)