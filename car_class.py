class car:
    def __init__(self, year, make):
        self.__year = year
        self.__make = make
        self.__speed = 0
    def return_speed(self):
        return self.__speed
    def acceleration(self):
        current_speed = self.__speed 
        new_speed = current_speed +5
        self.__speed = new_speed
    def brake(self):
        b_speed = self.__speed
        new_bspeed = b_speed - 5
        self.__speed = new_bspeed
    def set_year(self, year):
        self.__year = year
    def set_make(self, make):
        self.__make = make
    def get_make(self):
        return self.__make
    def get_year(self):
        return self.__year
        
     


   
    

    




