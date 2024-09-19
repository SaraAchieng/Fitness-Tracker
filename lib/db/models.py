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
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

engine = create_engine('sqlite:///fitness_database.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    workouts = relationship("Workout", back_populates="user")
    goals = relationship("Goal", back_populates="user")  # Add this relationship

class Workout(Base):
    __tablename__ = 'workouts'
    id = Column(Integer, primary_key=True)
    workout_type = Column(String, nullable=False)
    distance = Column(Float)  # Distance in kilometers
    steps = Column(Integer)  # Number of steps
    calories = Column(Float, nullable=False)  # Calories burned
    date = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="workouts")

class Goal(Base):
    __tablename__ = 'goals'
    id = Column(Integer, primary_key=True)
    goal_type = Column(String, nullable=False)  # Type of goal (steps, calories, distance)
    target_value = Column(Float, nullable=False)  # Target value for the goal (e.g., 10000 steps)
    is_achieved = Column(Boolean, default=False)  # Whether the goal is achieved or not
    user_id = Column(Integer, ForeignKey('users.id'))  # Link to the user
    user = relationship("User", back_populates="goals")  # Relationship back to User
     
     
if __name__ == "__main__":
    Base.metadata.create_all(engine)