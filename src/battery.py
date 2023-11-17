from datetime import datetime 

class Battery():
    def __init__(self, last_service_date: datetime, current_date:datetime):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service():
        pass
    

class SpindlerBattery(Battery):
    def __init__(self, last_service_date: datetime, current_date:datetime):
        super().__init__(last_service_date, current_date)

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False

class NubbinBattery(Battery):
    def __init__(self, last_service_date: datetime, current_date:datetime):
        super().__init__(last_service_date, current_date)

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False
  