from sklearn.ensemble import RandomForestRegressor
import pandas as pd

fake_weekly_data_rooms = pd.DataFrame([
    [1, 5, 12, 20],
    [1, 1, 15, 14],
    [1, 5, 12, 21],
    [1, 1, 12, 16],
    [1, 5, 12, 20],
    [1, 1, 12, 15],
    [1, 5, 12, 22],
    [2, 2, 21, 25],
    [2, 2, 13, 20],
    [2, 2, 21, 21],
    [2, 2, 15, 16],
    [2, 2, 21, 27],
    [2, 2, 13, 19],
    [2, 2, 20, 21]
], columns=['room', 'day_of_week', 'hour_of_day', 'temperature'])

fake_weekly_data_lights = pd.DataFrame([
    [1, 5, 12, 50],
    [2, 1, 15, 20],
    [1, 5, 12, 55],
    [2, 1, 12, 17],
    [1, 5, 12, 55],
    [2, 1, 12, 15],
    [1, 5, 12, 60],
    [3, 2, 21, 20],
    [3, 2, 13, 70],
    [3, 2, 21, 15],
    [3, 2, 15, 65],
    [3, 2, 21, 10],
    [3, 2, 13, 85],
    [3, 2, 20, 17]
], columns=['light', 'day_of_week', 'hour_of_day', 'intensity'])

fake_weekly_data_light_warmth = pd.DataFrame([ #2700-6500
    [1, 5, 12, 6000],
    [2, 1, 15, 4000],
    [1, 5, 12, 5700],
    [2, 1, 12, 3200],
    [1, 5, 12, 5500],
    [2, 1, 12, 4100],
    [1, 5, 12, 6100],
    [3, 2, 21, 3300],
    [3, 2, 13, 4100],
    [3, 2, 21, 3450],
    [3, 2, 15, 6200],
    [3, 2, 21, 3560],
    [3, 2, 13, 6300],
    [3, 2, 20, 3700]
], columns=['light', 'day_of_week', 'hour_of_day', 'warmth'])

class LightRegressor():
    def __init__(self):
        
        # Train temperature model
        temperature_model = RandomForestRegressor(n_estimators=10)
        X = fake_weekly_data_rooms[['room', 'day_of_week', 'hour_of_day']]
        y = fake_weekly_data_rooms['temperature']
     
        temperature_model.fit(X, y)
        self.temperature_model = temperature_model
        
        # Train light intensity model
        light_intensity_model = RandomForestRegressor(n_estimators=10)
        X = fake_weekly_data_lights[['light', 'day_of_week', 'hour_of_day']]
        y = fake_weekly_data_lights['intensity']
     
        light_intensity_model.fit(X, y)
        self.light_intensity_model = light_intensity_model
        
        # Train light warmth model
        light_warmth_model = RandomForestRegressor(n_estimators=10)
        X = fake_weekly_data_light_warmth[['light', 'day_of_week', 'hour_of_day']]
        y = fake_weekly_data_light_warmth['warmth']
     
        light_warmth_model.fit(X, y)
        self.light_warmth_model = light_warmth_model

    def predict_temperature(self, room_objs):
        """
            room_objs: list with format [[room_number(int), day_of_week(int), hour_of_day(int)],..]
        """
        return self.temperature_model.predict(pd.DataFrame(room_objs))
   
    def predict_light_intensity(self, light_objs):
        """
            light_objs: list with format [[light_number(int), day_of_week(int), hour_of_day(int)],..]
        """
        return self.light_intensity_model.predict(pd.DataFrame(light_objs))
   
    def predict_light_warmth(self, light_objs):
        """
            light_objs: list with format [[light_number(int), day_of_week(int), hour_of_day(int)],..]
        """
        return self.light_warmth_model.predict(pd.DataFrame(light_objs))
        