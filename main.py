from profile import create_profile, view_profile, edit_profile
from nutrition import log_nutrition, view_nutrition
from workouts import log_workout, view_workouts, edit_workout

def display_about():
    """Displays information about the app."""
    print("\nAbout Fit Track")
    print("This app is designed to help you track your fitness journey.")
    print("With this app, you can:")
    print("- Create and manage your personal profile with details like weight and body fat percentage.")
    print("- Log and review daily nutrition, including calories and macros.")
    print("- Record and review your workout sessions, with details on duration and calories burned.")
    print("The goal of this app is to support your fitness goals by providing a simple, efficient way to monitor your progress.")
    print("Enjoy your fitness journey, and let this app be your companion along the way!")

def display_welcome_message():
    """Displays a welcome message to the user when the app starts."""
    print("\nWelcome to Fit Track!")
    print("Track your fitness, nutrition, and workouts in one place.")
    print("Stay motivated and achieve your fitness goals with ease!")
    print("Let's get started. Choose an option from the menu below:")

def main_menu():
    """Displays the main menu and handles user input."""
    display_welcome_message()  # Show the welcome message when the app starts

    while True:
        print("\nFit Track Main Menu")
        print("1. Create Profile")
        print("2. View Profile")
        print("3. Edit Profile")
        print("4. Log Nutrition")
        print("5. View Nutrition")
        print("6. Log Workout")
        print("7. View Workouts")
        print("8. Edit Workout")  
        print("9. About")  
        print("10. Exit")  
        
        try:
            choice = int(input("Select an option (1-10): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")
            continue
        
        if choice == 1:
            create_profile()
        elif choice == 2:
            view_profile()
        elif choice == 3:
            edit_profile()
        elif choice == 4:
            log_nutrition()
        elif choice == 5:
            view_nutrition()
        elif choice == 6:
            log_workout()
        elif choice == 7:
            view_workouts()
        elif choice == 8:
            edit_workout()  # Call the edit_workout function here
        elif choice == 9:
            display_about()  # Show About
        elif choice == 10:
            print("Exiting the app. Please re-run the program if you want to see the main menu again. Goodbye!")  # Exit app
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 10. Note that only one command can be done at a time.")

if __name__ == "__main__":
    main_menu()