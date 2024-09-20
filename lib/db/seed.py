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
    users = create_users(6)  
    create_workouts(users, 10)  
    create_goals(users, 7)  
    
    print("Data seeded successfully!")


