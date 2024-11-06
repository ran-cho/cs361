import json
import os
from datetime import datetime

NUTRITION_FILE = "nutrition.json"

def log_nutrition():
    """Prompt user for nutrition details and save them to a JSON file with the date."""
    date = input("Enter the date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')

    try:
        calories = int(input("Enter calorie intake: "))
        protein = float(input("Enter protein intake (grams): "))
        carbs = float(input("Enter carb intake (grams): "))
        fats = float(input("Enter fat intake (grams): "))
    except ValueError:
        print("Invalid input. Calorie intake and macros must be numbers.")
        return

    nutrition_entry = {
        "date": date,
        "calories": calories,
        "protein": protein,
        "carbs": carbs,
        "fats": fats
    }

    if not os.path.exists(NUTRITION_FILE):
        data = []
    else:
        with open(NUTRITION_FILE, "r") as f:
            data = json.load(f)
    
    data.append(nutrition_entry)
    with open(NUTRITION_FILE, "w") as f:
        json.dump(data, f, indent=2)
    print("Nutrition log saved successfully!")


def view_nutrition():
    """Display all logged nutrition entries."""
    if not os.path.exists(NUTRITION_FILE):
        print("No nutrition data found. Please log your nutrition first.")
        return

    with open(NUTRITION_FILE, "r") as f:
        data = json.load(f)

    print("\nNutrition Log:")
    for entry in data:
        print(f"Date: {entry['date']}")
        print(f"Calories: {entry['calories']} kcal")
        print(f"Protein: {entry['protein']} g")
        print(f"Carbs: {entry['carbs']} g")
        print(f"Fats: {entry['fats']} g")
        print("-" * 20)
