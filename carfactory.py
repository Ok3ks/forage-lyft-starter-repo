from car import Car
from engine import Engine, CapuletEngine, WilloughbyEngine, SternmanEngine
from battery import NubbinBattery, SpindlerBattery, Battery
from datetime import datetime

#specify type of battery and engine
class CarFactory():
    def __init__(self, current_date:datetime, last_service_date:datetime, current_mileage:int, last_service_mileage:int):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def create_calliope(self):
        self.engine = Engine(self.last_service_mileage, self.current_mileage)
        self.battery = Battery(self.last_service_date, self.current_date)
        return Car(self.engine, self.battery)

    def create_glissade(self):
        self.engine = Engine(self.last_service_mileage, self.current_mileage)
        self.battery = Battery(self.last_service_date, self.current_date)
        return Car(self.engine, self.battery)

    def create_palindrome(self, warning_light_on:bool):
        self.engine = Engine(warning_light_on)
        self.battery = Battery(self.last_service_date, self.current_date)
        return Car(self.engine, self.battery)

    def create_rorschach(self):
        self.engine = Engine(self.last_service_mileage, self.current_mileage)
        self.battery = Battery(self.last_service_date, self.current_date)
        return Car(self.engine, self.battery)
    
    def create_thovex(self):
        self.engine = Engine(self.last_service_mileage, self.current_mileage)
        self.battery = Battery(self.last_service_date, self.current_date)
        return Car(self.engine, self.battery)