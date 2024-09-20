
import sys

from sqlalchemy import create_engine
from models import (create_user, update_user, delete_user, display_all_users, find_user_by_name, find_user_by_id, 
                    create_workout, update_goal, delete_workout, display_all_workouts, update_workout, find_workout_by_id,
                    create_goal, find_workout_by_type, delete_goal, display_all_goals, find_goal_by_id, find_goal_by_type)





def print_menu():
    print("1. Create User")
    print("2. Update User")
    print("3. Delete User")
    print("4. Display All Users")
    print("5. Find User by ID")
    print("6. Find User by Name")
    print("7. Create Workout")
    print("8. Update Workout")
    print("9. Delete Workout")
    print("10. Display All Workouts")
    print("11. Find Workout by ID")
    print("12. Find Workout by Type")
    print("13. Create Goal")
    print("14. Update Goal")
    print("15. Delete Goal")
    print("16. Display All Goals")
    print("17. Find Goal by ID")
    print("18. Find Goal by Type")
    print("19. Exit")


        
     

# Main loop for CLI
def main():
    while True:
        print_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            create_user()
        elif choice == "2":
            update_user()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            display_all_users()
        elif choice == "5":
            find_user_by_id()
        elif choice == "6":
            find_user_by_name()
        elif choice == "7":
            create_workout()
        elif choice == "8":
            update_workout()
        elif choice == "9":
            delete_workout()
        elif choice == "10":
            display_all_workouts()
        elif choice == "11":
            find_workout_by_id()
        elif choice == "12":
            find_workout_by_type()
        elif choice == "13":
            create_goal()
        elif choice == "14":
            update_goal()
        elif choice == "15":
            delete_goal()
        elif choice == "16":
            display_all_goals()
        elif choice == "17":
            find_goal_by_id()
        elif choice == "18":
            find_goal_by_type()
        elif choice == "19":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()


