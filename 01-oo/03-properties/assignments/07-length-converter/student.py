class LengthConverter:
    def __init__(self):
        # Initially, set the distance to 0 meters
        self.__distance_in_meter = 0
    
    @property
    def meter(self):
        # Return the distance in meters
        return self.__distance_in_meter
    
    @meter.setter
    def meter(self, value):
        # Convert the value to meters and store it
        self.__distance_in_meter = value
    
    @property
    def feet(self):
        # Convert the distance in meters to feet
        return round(self.__distance_in_meter * 3.28084, 3)
    
    @feet.setter
    def feet(self, value):
        # Convert the value in feet to meters and store it
        self.__distance_in_meter = value / 3.28084
    
    @property
    def inch(self):
        # Convert the distance in meters to inches
        return round(self.__distance_in_meter * 39.3701, 2)
    
    @inch.setter
    def inch(self, value):
        # Convert the value in inches to meters and store it
        self.__distance_in_meter = value / 39.3701
