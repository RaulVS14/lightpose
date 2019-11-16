import random


class Room():

    def __init__(self, x, y, x_size, y_size, name, room_id, capacity=5):
        self.x = x
        self.y = y
        self.x_size = x_size
        self.y_size = y_size
        self.name = name
        self.room_id = room_id
        self.lamp_power = 0
        self.room_temp = 22
        self.n_persons = 0
        self.capacity = capacity

    def is_in(self, user_x, user_y):
        cond1 = self.x <= user_x <= (self.x+self.x_size)
        cond2 = self.y <= user_y <= (self.y+self.y_size)
        return cond1 and cond2

    def set_lamp_power(self, lamp_power):
        self.lamp_power = int(lamp_power)

    def set_room_temp(self, room_temp):
        self.room_temp = int(room_temp)

    def add_person(self):
        self.n_persons = min(self.n_persons+1, self.capacity)

    def del_person(self):
        self.n_persons = max(self.n_persons-1, 0)

    def get_person_state(self):
        people = []
        delta_x = self.x_size / 3
        delta_y = 10
        for i in range(self.n_persons):
            people.append({
                'x': self.x + self.x_size/2 + random.uniform(-delta_x, delta_x),
                'y': 20 + self.y + self.y_size/2 + random.uniform(-delta_y, delta_y)
            })
        return people

    def get_room_state(self):

        lamp = 'rgba(255, 255, 0, {})'.format(self.lamp_power / 100)

        return {'x': self.x, 
                'y': self.y,
                'name': self.name,
                'lamp': lamp,
                'room_id': self.room_id,
                'n_persons': self.n_persons,
                'lamp_power': self.lamp_power,
                'room_temp': self.room_temp,
                'lamp_power_str': "Lights: {:d} %".format(self.lamp_power),
                'room_temp_str': "{:d} °C".format(self.room_temp),
                'x_size': self.x_size, 
                'y_size': self.y_size}
