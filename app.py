from flask import Flask, render_template
import json
import pprint

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/all')
def all_teachers():
    return render_template('all.html')


@app.route('/goals/<goal>/')
def goal():
    return render_template('goal.html')


@app.route('/profiles/<teacher_id>/')
def teachers_profiles(teacher_id):
    with open('output.json', 'r') as json_file:
        json_string = json_file.read()
        teachers_dictionary = json.loads(json_string)
        teacher_data = teachers_dictionary[int(teacher_id)]
        pprint.pprint(teacher_data)

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


@app.route("/request_done/")
def order_done():
    return render_template('request_done.html')


@app.route("/booking/<teacher_id>/<week_day>/<time>/")
def booking(teacher_id, week_day, time):
    with open('output.json', 'r') as json_file:
        json_string = json_file.read()
        teachers_dictionary = json.loads(json_string)
        teacher_data = teachers_dictionary[int(teacher_id)]
        teacher_name = teacher_data['name']
        pprint.pprint(teacher_data)
    return render_template('booking.html',
                           teacher_name=teacher_name, teacher_id=teacher_id,
                           week_day=week_day, time=time)


@app.route("/booking_done/")
def booking_done():
    return render_template('booking_done.html')


if __name__ == "__main__":
    app.run(debug=True)