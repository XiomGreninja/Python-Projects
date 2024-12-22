# Python Weight Converter
weight = float(input("Enter your weight: "))
unit = input("Kiligrams or Pounds? (K or L): ").strip().lower()

if unit == "K" or unit == "k":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "L" or unit == "l":
    weight = weight / 2.205
    unit = "Kgs."
else:
    print(f"{unit} was not valid")
    exit()

print(f"Your weight is: {round(weight,1)} {unit}")