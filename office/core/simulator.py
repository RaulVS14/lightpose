
class Simulation():

    def __init__(self):
        self.rooms = []
        self.controllers = []

    def add_person(self, user_x, user_y):
        for r in self.rooms:
            if r.is_in(user_x, user_y):
                r.add_person()
                print("Added person to {}".format(r.room_id))

    def del_person(self, user_x, user_y):
        for r in self.rooms:
            if r.is_in(user_x, user_y):
                r.del_person()

    def add_room(self, room):
        self.rooms.append(room)

    def add_controller(self, controller):
        self.controllers.append(controller)

    def step_run(self):
        for controller in self.controllers:
            for r in self.rooms:
                if controller.is_room_controlled(r.room_id):
                    state = r.get_room_state()
                    action = controller.predict(state)
                    r.set_lamp_power(action['lamp_power'])
                    r.set_room_temp(action['room_temp'])

    def get_state(self):
        
        persons = []
        for r in self.rooms:
            for p in r.get_person_state():
                persons.append(p)

        rooms = [r.get_room_state() for r in self.rooms]

        state = {
            'persons': persons,
            'rooms': rooms
        }
        return state
