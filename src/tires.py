from abc import ABC

class Tires(ABC):
    def needs_service():
        pass
    
class CarriganTires(Tires):
    def __init__(self,front_left, front_right, back_left, back_right):
       self.front_left = front_left
       self.front_right = front_right
       self.back_left = back_left
       self.back_right = back_right

    def sensors(self):
        return [self.front_left, self.front_right, self.back_left, self.back_right]

    def needs_service(self):
        check = [reading >= 0.9 for reading in self.sensors()]
        return True if any(check) else False

class OctoPrimeTires(Tires):
    def __init__(self,front_left, front_right, back_left, back_right):
       self.front_left = front_left
       self.front_right = front_right
       self.back_left = back_left
       self.back_right = back_right

    def sensors(self):
        return [self.front_left, self.front_right, self.back_left, self.back_right]

    def needs_service(self):
        return True if sum(self.sensors()) >= 3 else False