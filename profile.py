import json
import os

PROFILE_FILE = "profile.json"

def create_profile():
    """Prompt user for profile details and save them to a JSON file."""
    name = input("Enter your name: ")
    try:
        weight = float(input("Enter your weight (kg): "))
        body_fat = float(input("Enter your body fat percentage (%): "))
    except ValueError:
        print("Invalid input. Weight and body fat percentage must be numbers.")
        return

    profile = {
        "name": name,
        "weight": weight,
        "body_fat": body_fat
    }

    with open(PROFILE_FILE, "w") as f:
        json.dump(profile, f)
    print("Profile created successfully!")


def view_profile():
    """Display the profile details if they exist."""
    if not os.path.exists(PROFILE_FILE):
        print("No profile found. Please create one first.")
        return

    with open(PROFILE_FILE, "r") as f:
        profile = json.load(f)
        print("\nProfile Details:")
        print(f"Name: {profile['name']}")
        print(f"Weight: {profile['weight']} kg")
        print(f"Body Fat: {profile['body_fat']}%")


def edit_profile():
    """Edit an existing profile by updating one or more fields."""
    if not os.path.exists(PROFILE_FILE):
        print("No profile found. Please create one first.")
        return

    with open(PROFILE_FILE, "r") as f:
        profile = json.load(f)

    print("\nEdit Profile - Leave blank to keep current value")
    name = input(f"Enter new name (current: {profile['name']}): ") or profile['name']
    weight = input(f"Enter new weight (current: {profile['weight']} kg): ")
    body_fat = input(f"Enter new body fat % (current: {profile['body_fat']}%): ")

    # Update fields if new values are provided
    profile['name'] = name
    if weight:
        try:
            profile['weight'] = float(weight)
        except ValueError:
            print("Invalid input for weight. Value unchanged.")
    if body_fat:
        try:
            profile['body_fat'] = float(body_fat)
        except ValueError:
            print("Invalid input for body fat percentage. Value unchanged.")

    with open(PROFILE_FILE, "w") as f:
        json.dump(profile, f)
    print("Profile updated successfully!")
