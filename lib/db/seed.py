# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from models import User, Workout, Goal, Base

# # Connect to the SQLite database
# engine = create_engine('sqlite:///fitness_database.db')

# # Create a session to interact with the database
# Session = sessionmaker(bind=engine)
# session = Session()

# # Create some sample users
# user1 = User(name="Alice Smith", email="alice.smith@example.com")
# user2 = User(name="Bob Johnson", email="bob.johnson@example.com")

# # Create some sample workouts for the users
# workout1 = Workout(workout_type="Running", distance=5.0, steps=7000, calories=400, user=user1)
# workout2 = Workout(workout_type="Walking", distance=3.0, steps=4000, calories=200, user=user1)
# workout3 = Workout(workout_type="Cycling", distance=10.0, steps=0, calories=600, user=user2)

# # Create some goals for the users
# goal1 = Goal(goal_type="Steps", target_value=10000, is_achieved=False, user=user1)
# goal2 = Goal(goal_type="Calories", target_value=500, is_achieved=True, user=user2)

# # Add everything to the session
# session.add_all([user1, user2, workout1, workout2, workout3, goal1, goal2])

# # Commit the changes to the database
# session.commit()

# # Close the session
# session.close()

# print("Data seeded successfully!")

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Base, User, Workout, Goal

# Initialize Faker and SQLAlchemy
fake = Faker()
engine = create_engine('sqlite:///fitness_database.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create a function to add users
def create_users(n):
    users = []
    for _ in range(n):
        user = User(
            name=fake.name(),
            email=fake.unique.email()
        )
        users.append(user)
    session.add_all(users)
    session.commit()
    return users

# Create a function to add workouts
def create_workouts(users, n):
    workouts = []
    for _ in range(n):
        workout = Workout(
            workout_type=fake.word(),
            distance=fake.pyfloat(left_digits=3, right_digits=2, positive=True),
            steps=fake.random_int(min=1000, max=10000),
            calories=fake.pyfloat(left_digits=3, right_digits=1, positive=True),
            date=fake.date_time_this_year(),
            user_id=fake.random_element(elements=[user.id for user in users])
        )
        workouts.append(workout)
    session.add_all(workouts)
    session.commit()

# Create a function to add goals
def create_goals(users, n):
    goals = []
    for _ in range(n):
        goal = Goal(
            goal_type=fake.word(),
            target_value=fake.pyfloat(left_digits=3, right_digits=2, positive=True),
            is_achieved=fake.boolean(),
            user_id=fake.random_element(elements=[user.id for user in users])
        )
        goals.append(goal)
    session.add_all(goals)
    session.commit()

# Generate and add data
if __name__ == "__main__":
    # Create tables
    Base.metadata.create_all(engine)
    
    # Add users, workouts, and goals
    users = create_users(10)  # Create 10 users
    create_workouts(users, 20)  # Create 20 workouts
    create_goals(users, 15)  # Create 15 goals
    
    print("Data seeded successfully!")


