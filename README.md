# Flask Tutor Choice Website

This is a Flask-based website designed to help users choose an English tutor based on their learning goals. The website
offers a variety of tutors, and users can book lessons with them, as well as make specific requests regarding their
learning preferences.

Features
- Home Page: Displays a random selection of three tutors.
- All Tutors Page: Shows all available tutors, randomly shuffled.
- Tutor Search by Goal: Users can search for tutors based on their learning goals (e.g., speaking, grammar).
- Tutor Profiles: Detailed profiles for each tutor, showing their availability and other key information.
- Lesson Booking: Users can book lessons with their chosen tutor for a specific time and day.
- Request Form: Users can make specific requests (e.g., learning goals and preferred time), and the data is saved for
further processing.

## Installation

```bash
git clone https://github.com/haldaniko/TutorChoice-FlaskWebsite.git
cd TutorChoice-FlaskWebsite

# on macOS
python3 -m venv venv
source venv/bin/activate

# on Windows
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python app.py
```

The Website will be available at `http://127.0.0.1:5000/`

## Demo
![demo.png](screenshots%2Fdemo.png)
---
![demo2.png](screenshots%2Fdemo2.png)