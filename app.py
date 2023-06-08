from flask import Flask, render_template, request, redirect
import json
import random
import pprint

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    with open('output.json', 'r') as json_file:
        json_string = json_file.read()
        teachers_dictionary = json.loads(json_string)
        teachers_dict_3 = random.sample(teachers_dictionary, 3)
    return render_template('index.html', teachers_dict_3=teachers_dict_3)


@app.route('/all')
def all_teachers():
    with open('output.json', 'r') as json_file:
        json_string = json_file.read()
        teachers_dictionary = json.loads(json_string)
        random.shuffle(teachers_dictionary)
    return render_template('all.html', teachers_dictionary=teachers_dictionary)


@app.route('/goals/<client_goal>/')
def goal(client_goal):
    with open('output.json', 'r') as json_file:
        json_string = json_file.read()
        teachers_dictionary = json.loads(json_string)
        teachers_goal_dict = []
        for teacher in teachers_dictionary:
            for goal in teacher['goals']:
                if goal == client_goal:
                    teachers_goal_dict.append(teacher)

    return render_template('goal.html', client_goal=client_goal, teachers_goal_dict=teachers_goal_dict)


@app.route('/profiles/<teacher_id>/')
def teachers_profiles(teacher_id):
    with open('output.json', 'r') as json_file:
        json_string = json_file.read()
        teachers_dictionary = json.loads(json_string)
        teacher_data = teachers_dictionary[int(teacher_id)]
    busy_days = []
    for day, time in teacher_data['free'].items():
        is_busy = False
        for status in time.values():
            if status:
                is_busy = True
        if not is_busy:
            busy_days.append(day)

    return render_template('profile.html', teacher_data=teacher_data, busy_days=busy_days)


@app.route('/request/')
def order():
    return render_template('request.html')


@app.route("/request_done/", methods=['GET', 'POST'])
def order_done():
    if request.method == 'GET':
        return redirect('/request')
    else:
        clientGoal = request.form.get("goal")
        clientTime = request.form.get("time")
        clientName = request.form.get("clientName")
        clientPhone = request.form.get("clientPhone")

        new_data = {
            "clientGoal": clientGoal,
            "clientTime": clientTime,
            "clientName": clientName,
            "clientPhone": clientPhone,
        }

        try:
            with open('request.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
        new_key = str(len(data) + 1)
        data[new_key] = new_data
        with open('request.json', 'w') as file:
            json.dump(data, file, indent=2)
        print(clientGoal, clientName, clientTime, clientPhone)
        return render_template('request_done.html',
                               goal=clientGoal, time=clientTime,
                               name=clientName, phone=clientPhone)


@app.route("/booking/<teacher_id>/<week_day>/<time>/", methods=['GET', 'POST'])
def booking(teacher_id, week_day, time):
    with open('output.json', 'r') as json_file:
        json_string = json_file.read()
        teachers_dictionary = json.loads(json_string)
        teacher_data = teachers_dictionary[int(teacher_id)]
        teacher_name = teacher_data['name']
        teacher_picture = teacher_data['picture']
    return render_template('booking.html',
                           teacher_name=teacher_name, teacher_id=teacher_id,
                           week_day=week_day, time=time, teacher_picture=teacher_picture)


@app.route("/booking_done/", methods=['GET', 'POST'])
def booking_done():
    if request.method == 'GET':
        return redirect('/index')
    else:
        clientWeekday = request.form.get("clientWeekday")
        clientTime = request.form.get("clientTime")
        clientTeacher = request.form.get("clientTeacher")
        clientName = request.form.get("clientName")
        clientPhone = request.form.get("clientPhone")

        new_data = {
            "clientWeekday": clientWeekday,
            "clientTime": clientTime,
            "clientTeacher": clientTeacher,
            "clientName": clientName,
            "clientPhone": clientPhone
        }

        try:
            with open('booking.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
        new_key = str(len(data) + 1)
        data[new_key] = new_data
        with open('booking.json', 'w') as file:
            json.dump(data, file, indent=2)

        return render_template("booking_done.html",
                               day=clientWeekday, time=clientTime,
                               name=clientName, phone=clientPhone)


if __name__ == "__main__":
    app.run(debug=True)
