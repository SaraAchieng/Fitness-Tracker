# # models.py


# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
# from sqlalchemy.orm import relationship
# from datetime import datetime


# engine = create_engine('sqlite:///fitness_database.db')

# Base = declarative_base()

# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     email = Column(String, nullable=False, unique=True)
#     workouts = relationship("Workout", back_populates="user")
    
# class Workout(Base):
#     __tablename__ = 'workouts'
#     id = Column(Integer, primary_key=True)
#     workout_type = Column(String, nullable=False)
#     distance = Column(Float)  # Distance in kilometers
#     steps = Column(Integer)  # Number of steps
#     calories = Column(Float, nullable=False)  # Calories burned
#     date = Column(DateTime, default=datetime.utcnow)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     user = relationship("User", back_populates="workouts")   
    
# class Goal(Base):
#     __tablename__ = 'goals'
#     id = Column(Integer, primary_key=True)
#     goal_type = Column(String, nullable=False)  # Type of goal (steps, calories, distance)
#     target_value = Column(Float, nullable=False)  # Target value for the goal (e.g., 10000 steps)
#     is_achieved = Column(Boolean, default=False)  # Whether the goal is achieved or not
#     user_id = Column(Integer, ForeignKey('users.id'))  # Link to the user
#     user = relationship("User", back_populates="goals")
     
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean, Table, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate
from colorama import Fore, Style, init
init()



Base = declarative_base()

# Association table for many-to-many relationship between User and Workout
user_workout_association = Table(
    'user_workout_association', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('workout_id', Integer, ForeignKey('workouts.id'))
)

# Association table for many-to-many relationship between User and Goal
user_goal_association = Table(
    'user_goal_association', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('goal_id', Integer, ForeignKey('goals.id'))
)    

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String(), nullable=False, unique=True)
    workouts = relationship("Workout", backref=backref("user"))
    goals = relationship("Goal", backref=backref("user")) 
    workouts = relationship("Workout", secondary=user_workout_association, back_populates="users")
    goals = relationship("Goal", secondary=user_goal_association, back_populates="users") 
    
    def __repr__(self):
        return f"{self.id} {self.name} {self.email}"    

class Workout(Base):
    __tablename__ = 'workouts'
    id = Column(Integer, primary_key=True)
    workout_type = Column(String())
    distance = Column(Float())  # Distance in kilometers
    steps = Column(Integer())  # Number of steps
    calories = Column(Float())  # Calories burned
    date = Column(DateTime(), default=datetime.now())
    user_id = Column(Integer(), ForeignKey('users.id'))
    # user = relationship("User", backref=backref("workouts"))
    users = relationship("User", secondary=user_workout_association, back_populates="workouts")
    
    def __repr__(self):
        return f"{self.id} {self.workout_type} {self.distance} {self.steps} {self.calories} {self.date}"  



class Goal(Base):
    __tablename__ = 'goals'
    id = Column(Integer(), primary_key=True)
    goal_type = Column(String())  # Type of goal (steps, calories, distance)
    target_value = Column(Float())  # Target value for the goal (e.g., 10000 steps)
    is_achieved = Column(Boolean(), default=False)  # Whether the goal is achieved or not
    user_id = Column(Integer(), ForeignKey('users.id'))  # Link to the user
    # user = relationship("User", backref=backref("goals"))  # Relationship back to User
    users = relationship("User", secondary=user_goal_association, back_populates="goals")
    
    def __repr__(self):
        return f"{self.id} {self.goal_type} {self.target_value} {self.is_achieved}"
     
     
# if __name__ == "__main__":
    
engine = create_engine('sqlite:///fitness_database.db')
Base.metadata.create_all(engine)


engine = create_engine('sqlite:///fitness_database.db')
Session = sessionmaker(bind=engine)
session = Session()
    
    
    
    
    
    
    
    
    
# def create_user():
#     name = input(Fore.GREEN + "Enter name: " + Style.RESET_ALL)
#     email = input("Enter email: ")
#     user = User(name=name, email=email)
#     session.add(user)
#     session.commit()
#     print("User created.")


def create_user():
    # Prompt for user details
    name = input(Fore.GREEN + "Enter name: " + Style.RESET_ALL)
    email = input("Enter email: ")
    
    # Create a new User instance
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    
    # Prepare data for tabulate
    user_data = [[user.id, user.name, user.email]]
    
    print(Fore.CYAN + "\nUser Created:\n" + Style.RESET_ALL)
    print()
    print(tabulate(user_data, headers=["ID", "Name", "Email"], tablefmt="fancy_grid"))

def update_user():
    user_id = int(input("Enter user ID to update: "))
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        name = input("Enter new name: ")
        email = input("Enter new email: ")
        user.name = name
        user.email = email
        session.commit()
        print("User updated.")
    else:
        print("User not found.")






# def delete_user():
#     user_id = int(input("Enter user ID to delete: "))
#     user = session.query(User).filter_by(id=user_id).first()
#     if user:
#         session.delete(user)
#         session.commit()
#         print("User deleted.")
#     else:
#         print("User not found.")


def delete_user():
    # Prompt for the user ID to delete
    user_id = int(input("Enter user ID to delete: "))
    
    # Query the User with the given ID
    user = session.query(User).filter_by(id=user_id).first()
    
    if user:
        # Prepare data for tabulate to display the user being deleted
        user_data = [[user.id, user.name, user.email]]
        
        print(Fore.CYAN + "\nUser to be Deleted:\n" + Style.RESET_ALL)
        print(tabulate(user_data, headers=["ID", "Name", "Email"], tablefmt="fancy_grid"))
        
        # Confirm deletion
        confirm = input(Fore.RED + "Are you sure you want to delete this user? (yes/no): " + Style.RESET_ALL)
        if confirm.lower() == 'yes':
            session.delete(user)
            session.commit()
            print("User deleted.")
        else:
            print("Deletion canceled.")
    else:
        print("User not found.")

def display_all_users():
    users = session.query(User).all()
    if users:
        for user in users:
            print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
    else:
        print("No users found.")

def find_user_by_id():
    user_id = int(input("Enter user ID: "))
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
    else:
        print("User not found.")

def find_user_by_name():
    name = input("Enter user name: ")
    user = session.query(User).filter_by(name=name).first()
    if user:
        print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
    else:
        print("User not found.")

# Functions for Workout
def create_workout():
    workout_type = input("Enter workout type: ")
    distance = float(input("Enter distance (km): "))
    steps = int(input("Enter number of steps: "))
    calories = float(input("Enter calories burned: "))
    user_id = int(input("Enter user ID: "))
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        workout = Workout(workout_type=workout_type, distance=distance, steps=steps, calories=calories, user_id=user.id)
        session.add(workout)
        session.commit()
        print("Workout created.")
    else:
        print("User not found.")

def update_workout():
    workout_id = int(input("Enter workout ID to update: "))
    workout = session.query(Workout).filter_by(id=workout_id).first()
    if workout:
        workout_type = input("Enter new workout type: ")
        distance = float(input("Enter new distance (km): "))
        steps = int(input("Enter new number of steps: "))
        calories = float(input("Enter new calories burned: "))
        workout.workout_type = workout_type
        workout.distance = distance
        workout.steps = steps
        workout.calories = calories
        session.commit()
        print("Workout updated.")
    else:
        print("Workout not found.")

def delete_workout():
    workout_id = int(input("Enter workout ID to delete: "))
    workout = session.query(Workout).filter_by(id=workout_id).first()
    if workout:
        session.delete(workout)
        session.commit()
        print("Workout deleted.")
    else:
        print("Workout not found.")

# def display_all_workouts():
#     workouts = session.query(Workout).all()
#     if workouts:
#         for workout in workouts:
#             print(f"ID: {workout.id}, Type: {workout.workout_type}, Distance: {workout.distance} km, Steps: {workout.steps}, Calories: {workout.calories}")
#     else:
#         print("No workouts found.")

def display_all_workouts():
    workouts = session.query(Workout).all()
    
    if workouts:
        # Prepare data for tabulate
        workout_data = [
            [workout.id, workout.workout_type, workout.distance, workout.steps, workout.calories]
            for workout in workouts
        ]
        
        print("\nAll Workouts:\n")
        print(tabulate(workout_data, headers=["ID", "Type", "Distance (km)", "Steps", "Calories"], tablefmt="fancy_grid"))
    else:
        print("No workouts found.")

def find_workout_by_id():
    workout_id = int(input("Enter workout ID: "))
    workout = session.query(Workout).filter_by(id=workout_id).first()
    if workout:
        print(f"ID: {workout.id}, Type: {workout.workout_type}, Distance: {workout.distance} km, Steps: {workout.steps}, Calories: {workout.calories}")
    else:
        print("Workout not found.")

def find_workout_by_type():
    workout_type = input("Enter workout type: ")
    workouts = session.query(Workout).filter_by(workout_type=workout_type).all()
    if workouts:
        for workout in workouts:
            print(f"ID: {workout.id}, Type: {workout.workout_type}, Distance: {workout.distance} km, Steps: {workout.steps}, Calories: {workout.calories}")
    else:
        print("No workouts found.")

# Functions for Goal
def create_goal():
    goal_type = input("Enter goal type: ")
    target_value = float(input("Enter target value: "))
    user_id = int(input("Enter user ID: "))
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        goal = Goal(goal_type=goal_type, target_value=target_value, user_id=user.id)
        session.add(goal)
        session.commit()
        print("Goal created.")
    else:
        print("User not found.")

def update_goal():
    goal_id = int(input("Enter goal ID to update: "))
    goal = session.query(Goal).filter_by(id=goal_id).first()
    if goal:
        goal_type = input("Enter new goal type: ")
        target_value = float(input("Enter new target value: "))
        goal.goal_type = goal_type
        goal.target_value = target_value
        session.commit()
        print("Goal updated.")
    else:
        print("Goal not found.")

def delete_goal():
    goal_id = int(input("Enter goal ID to delete: "))
    goal = session.query(Goal).filter_by(id=goal_id).first()
    if goal:
        session.delete(goal)
        session.commit()
        print("Goal deleted.")
    else:
        print("Goal not found.")

def display_all_goals():
    goals = session.query(Goal).all()
    if goals:
        for goal in goals:
            print(f"ID: {goal.id}, Type: {goal.goal_type}, Target Value: {goal.target_value}")
    else:
        print("No goals found.")

def find_goal_by_id():
    goal_id = int(input("Enter goal ID: "))
    goal = session.query(Goal).filter_by(id=goal_id).first()
    if goal:
        print(f"ID: {goal.id}, Type: {goal.goal_type}, Target Value: {goal.target_value}")
    else:
        print("Goal not found.")

def find_goal_by_type():
    goal_type = input(Fore.GREEN + "Enter goal type: " + Style.RESET_ALL)
    goals = session.query(Goal).filter_by(goal_type=goal_type).all()
    
    if goals:
        # Prepare data for tabulate
        goal_data = [[goal.id, goal.goal_type, goal.target_value, goal.is_achieved] for goal in goals]
        print(Fore.CYAN + "\n Goals Found " + Style.RESET_ALL)
        print()
        print(tabulate(goal_data, headers=["ID", "Type", "Target Value", "Achieved"], tablefmt="fancy_grid"))
    else:
        print(Fore.RED + "No goals found." + Style.RESET_ALL)
        
        



   
    
    
   
        