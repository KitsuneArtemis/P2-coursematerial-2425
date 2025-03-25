class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    @property
    def hours(self):
        return self._hours
    
    @hours.setter
    def hours(self, value):
        if 0 <= value <= 23:
            self._hours = value
        else:
            raise ValueError("Hours must be between 0 and 23")
    
    @property
    def minutes(self):
        return self._minutes
    
    @minutes.setter
    def minutes(self, value):
        if 0 <= value <= 59:
            self._minutes = value
        else:
            raise ValueError("Minutes must be between 0 and 59")
    
    @property
    def seconds(self):
        return self._seconds
    
    @seconds.setter
    def seconds(self, value):
        if 0 <= value <= 59:
            self._seconds = value
        else:
            raise ValueError("Seconds must be between 0 and 59")
