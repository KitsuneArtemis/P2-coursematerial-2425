# Write your code here
class BMICalculator:
    def __init__(self, weight_in_kg, height_in_m):
        self.weight_in_kg = weight_in_kg
        self.height_in_m = height_in_m
    
    @property
    def bmi(self):
        return round(self.weight_in_kg / (self.height_in_m ** 2), 2)
    
    @property
    def category(self):
        bmi_value = self.bmi
        if bmi_value < 18.5:
            return "underweight"
        elif bmi_value < 25:
            return "normal"
        else:
            return "overweight"
