# EduPro - Study Enhancement Flask Web App

#### Description:

EduPro is a user-friendly and intuitive Flask web application designed to assist students in enhancing their study habits and productivity. The app combines two essential tools – a timer and a calendar – to create an optimal environment for effective learning. With EduPro, students can manage their study sessions more efficiently and stay organized throughout their academic journey.

## Features

- **Study Timer**: EduPro features a built-in study timer that employs the Pomodoro technique to help students maintain focused and productive study sessions. Users can set customizable study and break durations, allowing them to work in concentrated bursts while avoiding burnout.

- **Interactive Calendar**: The integrated calendar enables students to schedule their study sessions, assignments, and exams in a visually appealing and organized manner. This helps students plan ahead and allocate time appropriately for various subjects and tasks.

- **Todo List**: Stay on top of your tasks with the new todo list feature. Add, complete, and delete tasks to keep track of your assignments, readings, and other responsibilities.

- **Setttings**: Customize your study experience with the app's settings. Adjust the timer durations for each state—study, short break, and long break—to cater to your productivity preferences. Additionally, conveniently modify your password through the settings menu to maintain account security.

- **User Authentication**: EduPro ensures user privacy and security by implementing a robust user authentication system. Each user can have a personalized profile with their timer preferences and calendar events.

## How to Use

1. **Sign Up/Log In**: Create an account or log in to your existing account to access the app's features.

2. **Timer**: Set your desired study duration and break time, then start the timer. The app will notify you when it's time to take a break or resume studying.

3. **Calendar**: Use the interactive calendar to schedule study sessions, assignments, and exams. You can add and delete events using the bottom right buttons of the page.

4. **Todo List**: Manage your tasks by adding them to the todo list. Check them off when completed and remove tasks you no longer need.

5. **Settings**: Change the settings of your timer for an enhanced expirience and change your password if needed.

6. **Log out**: When you're done using EduPro, log out of your account to ensure your privacy and security. Click on the "Log out" button to end your session.

## Structure

EduPro's codebase is organized into the following main directories and files:

- `app.py`: This file contains the main application code, including routes, templates, and static assets.
- `helpers.py`: Contains some functions used in in `app.py` like `apology`
- `templates/`: Here you'll find the HTML templates used to render the app's frontend.
- `static/`: This directory hosts static files such as stylesheets, JavaScript files, and images.
- `requirements.txt`: Lists all the Python packages required for running the application.
- `final.db`: This file contains all the data from users like timer preferences and calendar events.

## Installation

To run EduPro locally, follow these steps:

1. Clone this repository:

```
git clone https://github.com/hanvi10/edupro.git
```

2. Navigate to the project directory:

```
cd edupro
```

3. Install dependencies using pip:

```
pip install -r requirements.txt
```

4. Run the Flask development server:

```
flask run
```

5. Access the app in your web browser at `http://localhost:5000`.

## Credits

EduPro was developed by Han Virgili Phan. I acknowledge the contributions of various open-source libraries and tools that made this project possible.

## Feedback and Support

If you encounter any issues, have suggestions, or need assistance, please [submit an issue](https://github.com/hanvi10/edupro/issues) on our GitHub repository.

We hope EduPro significantly enhances your study experience and helps you achieve academic success. Happy studying!
