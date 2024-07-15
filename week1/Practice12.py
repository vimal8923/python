countries = {
    'India': {'capital': 'New Delhi', 'population': 1380004385},
    'china': {'capital': 'Beijing', 'population': 215420004},
    'japan': {'capital': 'tokyo', 'population': 140940343}
}
print("Initial Dictionary: ", countries)
capital = countries['India']['capital']
print("\nPrinting the capital of one country: ")
print("Capital of India: ", capital)
countries['china']['population'] =55675688
print("\n  Update the population of china country")
print("\nFinal dictionary: ", countries)