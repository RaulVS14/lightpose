
class BasicController():

    def __init__(self):
        self.rooms_ids = {}

    def set_rooms(self, room_ids):
        self.rooms_ids = room_ids

    def is_room_controlled(self, room_id):
        return room_id in self.rooms_ids

    def predict(self, state):
        n = state['n_persons']
        current_power = state['lamp_power']
        current_temp = state['room_temp']
        action = {'lamp_power': current_power, 'room_temp': current_temp}
        if(n == 0):
            action['lamp_power'] = max(current_power-20, 0)
            action['room_temp'] = 18
        else:
            action['lamp_power'] = min(40+20*n, 100.0)
            action['room_temp'] = max(22 - n, 18)
        return action


class LightRegressorController():

    def __init__(self):
        self.rooms_ids = {}

    def set_rooms(self, room_ids):
        self.rooms_ids = room_ids

    def is_room_controlled(self, room_id):
        return room_id in self.rooms_ids

    def predict(self, state):
        n = state['n_persons']
        current_power = state['lamp_power']
        current_temp = state['room_temp']
        action = {'lamp_power': current_power, 'room_temp': current_temp}
        if(n == 0):
            action['lamp_power'] = max(current_power-10, 0)
            action['room_temp'] = 18
        else:
            action['lamp_power'] = min(80+20*n, 100.0)
            action['room_temp'] = max(22 - n, 18)
        return action


class PersonalController():

    def __init__(self):
        self.rooms_ids = {}

    def set_rooms(self, room_ids):
        self.rooms_ids = room_ids

    def is_room_controlled(self, room_id):
        return room_id in self.rooms_ids

    def predict(self, state):
        n = state['n_persons']
        current_power = state['lamp_power']
        current_temp = state['room_temp']
        action = {'lamp_power': current_power, 'room_temp': current_temp}
        if(n == 0):
            action['lamp_power'] = 0
            action['room_temp'] = 18
        else:
            action['lamp_power'] = 90
            action['room_temp'] = 25
        return action
