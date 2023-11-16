from car import Car

class Engine():
    def __init__(self, current_mileage:int, last_service_mileage:int):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
    
class WilloughbyEngine(Engine):
    def __init__(self, current_mileage:int, last_service_mileage:int):
        super().__init__(last_service_mileage, current_mileage)

    def needs_service(self):
        pass

class CapuletEngine(Engine):
    def __init__(self, current_mileage:int, last_service_mileage:int):
        super().__init__(last_service_mileage, current_mileage)

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000
    
class SternmanEngine(Engine):
    def __init__(self, last_service_date, warning_light_is_on:bool =False):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        pass
