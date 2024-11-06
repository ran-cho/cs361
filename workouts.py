import os
import json
from datetime import datetime

WORKOUTS_FILE = "workouts.json"

def log_workout():
    """Prompt user for workout details and save them to a JSON file."""
    date = input("Enter the date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')

    workout_name = input("Enter workout name: ")

    try:
        duration = float(input("Enter duration (minutes): "))
        calories_burned = int(input("Enter calories burned: "))
    except ValueError:
        print("Invalid input. Duration must be a number and calories must be an integer.")
        return

    workout_entry = {
        "date": date,
        "workout_name": workout_name,
        "duration": duration,
        "calories_burned": calories_burned
    }

    # Load existing workouts from the file
    if os.path.exists(WORKOUTS_FILE):
        with open(WORKOUTS_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(workout_entry)

    with open(WORKOUTS_FILE, "w") as f:
        json.dump(data, f, indent=2)

    print("Workout log saved successfully!")

def view_workouts():
    """Display all logged workout entries."""
    if not os.path.exists(WORKOUTS_FILE):
        print("No workout data found. Please log your workouts first.")
        return

    with open(WORKOUTS_FILE, "r") as f:
        data = json.load(f)

    if not data:
        print("No workout records available.")
        return

    print("\nWorkout Log:")
    for idx, entry in enumerate(data, 1):
        date = entry.get('date', 'Unknown Date')
        workout_name = entry.get('workout_name', 'Unknown Workout')
        duration = entry.get('duration', 'Unknown Duration')
        calories_burned = entry.get('calories_burned', 'Unknown Calories')

        print(f"{idx}. Date: {date}, Workout: {workout_name}, Duration: {duration} minutes, Calories Burned: {calories_burned} kcal")

def edit_workout():
    """Allow the user to edit an existing workout."""
    if not os.path.exists(WORKOUTS_FILE):
        print("No workout data found. Please log your workouts first.")
        return

    with open(WORKOUTS_FILE, "r") as f:
        data = json.load(f)

    if not data:
        print("No workout records available.")
        return

    # Display existing workouts
    print("\nSelect the workout to edit:")
    for idx, entry in enumerate(data, 1):
        date = entry.get('date', 'Unknown Date')
        workout_name = entry.get('workout_name', 'Unknown Workout')
        print(f"{idx}. {date} - {workout_name}")

    try:
        # Let the user choose which workout to edit by index
        workout_index = int(input("Enter the number of the workout to edit: ")) - 1
        if workout_index < 0 or workout_index >= len(data):
            print("Invalid selection. No such workout.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    workout_to_edit = data[workout_index]
    print(f"\nEditing workout: {workout_to_edit['workout_name']} on {workout_to_edit['date']}")

    # Edit workout details
    workout_name = input(f"Enter new workout name (current: {workout_to_edit['workout_name']}): ")
    duration = input(f"Enter new duration (current: {workout_to_edit['duration']} minutes): ")
    calories_burned = input(f"Enter new calories burned (current: {workout_to_edit['calories_burned']} kcal): ")

    # Apply changes if not left blank
    if workout_name:
        workout_to_edit['workout_name'] = workout_name
    if duration:
        try:
            workout_to_edit['duration'] = float(duration)
        except ValueError:
            print("Invalid input for duration. Keeping the old value.")
    if calories_burned:
        try:
            workout_to_edit['calories_burned'] = int(calories_burned)
        except ValueError:
            print("Invalid input for calories burned. Keeping the old value.")

    # Save the updated list back to the file
    with open(WORKOUTS_FILE, "w") as f:
        json.dump(data, f, indent=2)

    print("Workout updated successfully!")
