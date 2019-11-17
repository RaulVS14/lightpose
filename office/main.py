from flask import Flask, request, render_template, jsonify, redirect

from core.elements import Room
from core.simulator import Simulation
from core.controllers import BasicController, LightRegressorController, PersonalController


app = Flask(__name__, static_url_path='/static')

# ------------------------------
# Create simulation
# ------------------------------
sim = Simulation()

# ------------------------------
# Add rooms
# ------------------------------
sim.add_room(Room(0, 0, 200, 200, 'Room 01', room_id='r101'))
sim.add_room(Room(200, 0, 200, 200, 'Room 02', room_id='r102'))
sim.add_room(Room(400, 0, 200, 200, 'Room 03', room_id='r103'))
sim.add_room(Room(600, 0, 200, 200, 'Room 04', room_id='r104'))
sim.add_room(Room(800, 0, 200, 200, 'Room 05', room_id='r105'))
sim.add_room(Room(1000, 0, 200, 200, 'Room 06', room_id='r106'))

sim.add_room(Room(0, 200, 200, 200, 'Room 14', room_id='r114'))
sim.add_room(Room(1000, 200, 200, 200, 'Room 07', room_id='r107'))
sim.add_room(Room(600, 200, 400, 200, 'Meeting', room_id='m101'))

sim.add_room(Room(0, 400, 200, 200, 'Room 13', room_id='r113'))
sim.add_room(Room(200, 400, 200, 200, 'Room 12', room_id='r112'))
sim.add_room(Room(400, 400, 200, 200, 'Room 11', room_id='r111'))
sim.add_room(Room(600, 400, 200, 200, 'Room 10', room_id='r110'))
sim.add_room(Room(800, 400, 200, 200, 'Room 09', room_id='r109'))
sim.add_room(Room(1000, 400, 200, 200, 'Room 08', room_id='r108'))

# ------------------------------
# Add controllers
# ------------------------------
basic_controller = BasicController()
basic_controller.set_rooms({
    'r103', 'r104', 'r105', 'r106', 'r107', 'r108', 'r109', 'r110',
    'r111', 'r112', 'r113', 'r114', 'm101'
})
sim.add_controller(basic_controller)

regressor_controller = LightRegressorController()
regressor_controller.set_rooms({'r101', 'r102'})
sim.add_controller(regressor_controller)

personal_controller = PersonalController()
personal_controller.set_rooms({'r113'})
sim.add_controller(personal_controller)


@app.route('/')
def serve_dashboard():
    context = {}
    return render_template('main.html', context=context)


@app.route('/update/power')
def update_power():

    room_id = request.args.get('id', None)
    lamp_power = int(request.args.get('power', 0))
    data = {
        'status': 'nop'
    }
    for r in sim.rooms:
        if r.room_id == room_id and lamp_power is not None:
            r.lamp_power = min(max(lamp_power, 0), 100)
            data['status'] = 'done'

    return jsonify(data), 200


@app.route('/update/user')
def update_user():
    user_x = float(request.args.get('x', None))
    user_y = float(request.args.get('y', None))
    a = request.args.get('a', None)
    if a == 'add':
        sim.add_person(user_x, user_y)
    else:
        sim.del_person(user_x, user_y)

    data = {'status': 'done'}
    return jsonify(data), 200


@app.route('/run/json')
def get_run():

    sim.step_run()

    data = {
        'state_data': sim.get_state()
    }
    return jsonify(data), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
