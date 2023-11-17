from abc import ABC
from datetime import datetime

class Engine(ABC):
    def needs_service():
        pass
    
class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage:int, current_mileage:int,):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
            return self.current_mileage - self.last_service_mileage > 60000
    
class CapuletEngine(Engine):
    def __init__(self, last_service_mileage:int, current_mileage:int,):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return (self.current_mileage - self.last_service_mileage) > 30000
    
class SternmanEngine(Engine):
    def __init__(self, last_service_date, warning_light_is_on:bool =False):
        self.last_service_date = last_service_date
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        return self.warning_light_is_on
