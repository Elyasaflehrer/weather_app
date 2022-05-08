class DataWeather:
    def __init__(self, day, temp_day, temp_night, humidity, icon, description, wind_speed, date):
        self.day = day
        self.temp_day = temp_day
        self.temp_night = temp_night
        self.humidity = humidity
        self.icon = icon
        self.description = description
        self.wind_speed = wind_speed
        self.date = date

    def get_day(self):
        return self.day

    def get_temp_day(self):
        return self.temp_day

    def get_temp_night(self):
        return self.temp_night

    def get_humidity(self):
        return self.humidity

    def get_icon(self):
        return self.icon

    def get_description(self):
        return self.description

    def get_windSpeed(self):
        return self.wind_speed

    def get_date(self):
        return self.date
