from car import Car
from datetime import datetime 

class Battery():
    def __init__(self, last_service_date: datetime, current_date:datetime):
        self.last_service_date = last_service_date
        self.current_date = current_date
    

class SpindlerBattery(Battery):
    def __init__(self, last_service_date: datetime, current_date:datetime):
        super().__init__(last_service_date, current_date)

    def needs_service(self):
        pass

class NubbinBattery(Battery):
    def __init__(self, last_service_date: datetime, current_date:datetime):
        super().__init__()

    def needs_service(self):
        pass
  