from abc import ABC, abstractmethod
from src.battery import Battery
from src.engine import Engine

from src.engine import Engine, CapuletEngine, WilloughbyEngine, SternmanEngine
from src.battery import NubbinBattery, SpindlerBattery
from datetime import datetime

class Car():
    def __init__(self, engine:Engine, battery:Battery):
        self.engine = engine
        self.battery= battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()

class CarFactory():
    def __init__(self, current_date:datetime, last_service_date:datetime, current_mileage:int, last_service_mileage:int):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def create_calliope(self):
        engine = CapuletEngine(self.last_service_mileage, self.current_mileage)
        battery = SpindlerBattery(self.last_service_date, self.current_date)
        return Car(engine, battery)

    def create_glissade(self):
        engine = WilloughbyEngine(self.last_service_mileage, self.current_mileage)
        battery = NubbinBattery(self.last_service_date, self.current_date)
        return Car(engine, battery)

    def create_palindrome(self, warning_light_on:bool):
        engine = SternmanEngine(self.last_service_date, warning_light_is_on = warning_light_on)
        battery = SpindlerBattery(self.last_service_date, self.current_date)
        return Car(engine, battery)

    def create_rorschach(self):
        engine = WilloughbyEngine(self.last_service_mileage, self.current_mileage)
        battery = NubbinBattery(self.last_service_date, self.current_date)
        return Car(engine, battery)
    
    def create_thovex(self):
        engine = CapuletEngine(self.last_service_mileage, self.current_mileage)
        battery = NubbinBattery(self.last_service_date, self.current_date)
        return Car(engine, battery)