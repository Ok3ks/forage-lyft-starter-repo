from abc import ABC, abstractmethod

from battery import Battery
from engine import Engine

class Car():
    def __init__(self, engine:Engine, battery:Battery):
        self.engine = engine
        self.battery= battery

    def needs_service(self):
        return True if self.engine.needs_service() or self.battery.needs_service() else False
