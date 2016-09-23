mealCost = float(input())

tipPercent = int(input())
tipPercent = mealCost * (tipPercent/100)

taxPercent = int(input())
taxPercent = mealCost * (taxPercent/100)

totalCost = round(mealCost + tipPercent + taxPercent)

print("The total meal cost is", totalCost, "dollars.")

