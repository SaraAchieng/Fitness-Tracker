# Overview
The Fitness Tracker CLI is a command-line interface (CLI) application designed to help users track their workouts and fitness goals. Users can create and manage their profiles, log various workouts, and set fitness goals such as steps, calories, or distance targets. The application makes use of a simple SQLite database to persist data and provides various functionalities for users to view, update, and delete their records.

This CLI uses libraries such as SQLAlchemy for database operations, Tabulate for table formatting, and Colorama for colorizing the CLI interface to improve user experience.

## Features
   # User Management:
    .Create a user with a name and email.
    .Update user details.
    .Delete a user after confirmation.
    .Display all users.
    .Find a user by ID or name.

   # Workout Management:
    .Log a workout (e.g., running, walking) with details such as distance, steps, and calories burned.
    .Update workout records.
    .Delete workouts.
    .Display all logged workouts.
    .Find workouts by ID or type.

   # Goal Management:
    .Create a goal (e.g., steps, calories, distance).
    .Update a goal (change the goal type or target value).
    .Delete goals.
    .Display all fitness goals.
    .Find goals by ID or type.

   # Data Persistence:
   - All data, including users, workouts, and goals, is stored in an SQLite database (fitness_database.db), ensuring persistence between sessions.

   # Colorful CLI:
   - The application uses the Colorama library to make the CLI more visually appealing by using different colors for prompts, messages, and tables.

   # Formatted Output:
   - The Tabulate library is used to display tables in a clear and readable format, especially when showing user, workout, or goal data.
    

## Technologies Used  
   . Python
   . SQLite3
   . Tabulate - For displaying tabular data in the terminal.
   . Colorama - For styling terminal outputs.
   . Virtual environment  
   . Pipenv to manage dependencies (or you can use pip).

## Setup & Installation
   . Prerequisites
   - The project is written in Python, so you'll need Python 3 installed

   To get a local copy of the project up and running, follow these steps:

     1. *Clone the Repository:*
      git clone https://github.com/SaraAchieng/Fitness-Tracker
   
     2. *Install Dependencies:*
      pipenv install

     3. *Generating Your Database:*
      Once you're in your environment, you can start development wherever you'd like.
      We think it's easiest to start with setting up your database.

     `cd` into the `lib/db` directory, then run `alembic init migrations` to set up
      Alembic. Modify line 58 in `alembic.ini` to point to the database you intend to
      create, then replace line 21 in `migrations/env.py` with the following:

      ```py
      from models import Base
      target_metadata = Base.metadata
      ```

      We haven't created our `Base` or any models just yet, but we know where they're
      going to be. Navigate to `models.py` and start creating those models. Remember
      to regularly run `alembic revision --autogenerate -m'<descriptive message>'` and
      `alembic upgrade head` to track your modifications to the database and create
      checkpoints in case you ever need to roll those modifications back.

      If you want to seed your database, now would be a great time to write out your
      `seed.py` script and run it to generate some test data. You may want to use
      Pipenv to install Faker to save you some time. 

     4. *Running the Application:*
      To start the application, ensure you are in the project directory and run the main script. For example:
        pipenv shell
        python cli.py

    


## Database Models
  # User Model
    Attributes:
      id: Integer (Primary Key)
      name: String
      email: String (Unique, Non-nullable)
    Relationships:
      One-to-many with Workout.
      One-to-many with Goal.
  # Workout Model
    Attributes:
      id: Integer (Primary Key)
      workout_type: String
      distance: Float (in kilometers)
      steps: Integer
      calories: Float (calories burned)
      date: DateTime (defaults to the current date and time)
      user_id: ForeignKey (references User)
  # Goal Model
    Attributes:
      id: Integer (Primary Key)
      goal_type: String (e.g., Steps, Calories, Distance)
      target_value: Float (target value to achieve)
      is_achieved: Boolean (defaults to False)
      user_id: ForeignKey (references User)
        

     

## Project Structure
*The current project structure:*

FITNESS-TRACKER/
.
├── alembic.ini
├── cli.py
├── fitness_database.db
├── migrations
│   ├── README
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       ├── 06038a6fc4ff_added_user_model.py
│       ├── 1428f3f9a93d_create_goals_table.py
│       ├── 6afaf1651dfd_added_goal_model.py
│       ├── bcd73505d924_empty_init.py
│       └── ee598f53a603_added_workout_model.py
├── models.py
└── seed.py
    

## Contributing

Contributions are welcome! If you have any suggestions, bug reports or feature requests please create an issue or submit a pull request.

If you wish to contribute follow the steps below:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/your-feature).
3. Make your changes and commit them (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature/your-feature).
5. Open a pull request.

## Support & Contact
  - email :: achieng997@gmail.com

## License
*Licenced under the MIT License Copyright (c) 2024 **Sara Achieng


    


