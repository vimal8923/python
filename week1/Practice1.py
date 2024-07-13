integers = [1,2,3,4,5,6,7,8,9,10]
print(integers)
squared_integer= [x**2 for x in integers]
print(squared_integer)

print("--------------------------------------------------------------------------------")

number=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(number)
number[2]= 50
print(number)

print("---------------------------------------------------------------------------------------------------------")

number=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(number)
number.insert(5,25)
print(number)

print("---------------------------------------------------------------------------------")
number=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(number)
number.pop(-1)
print(number)
