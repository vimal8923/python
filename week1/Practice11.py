cities = {"pune": "1.5 crore", "Kolkata ": "2 crore", "Ahmedabad ": "1.9 crore", "Mumbai": "10.4 crore", "Delhi": "5.5 crore"}
print(cities)

population_of_city= cities.get("kolkata")
print("\nUse the get method to access the population of a specific city: ",population_of_city)

remove_city = cities.pop("Delhi")
print("\nUse the pop method to remove a city from the dictionary: ",remove_city)

print("\nFinal dictionary: ", cities)


