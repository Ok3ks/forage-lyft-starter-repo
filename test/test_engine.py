
import unittest
from datetime import datetime

from src.engine import WilloughbyEngine
from src.engine import CapuletEngine
from src.engine import SternmanEngine

class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60_001
        last_mileage =0

        Engine = WilloughbyEngine(last_mileage, current_mileage)
        self.assertTrue(Engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 59_999
        last_mileage = 0

        Engine = WilloughbyEngine(last_mileage, current_mileage)
        self.assertFalse(Engine.needs_service())

class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30_001
        last_mileage =0

        Engine = CapuletEngine(last_mileage, current_mileage)
        self.assertTrue(Engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 29_999
        last_mileage = 0

        Engine = CapuletEngine(last_mileage, current_mileage)
        self.assertFalse(Engine.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True
        last_service_date = datetime.today().date()

        Engine = SternmanEngine(last_service_date, warning_light_is_on)
        self.assertTrue(Engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False
        last_service_date = datetime.today().date()

        Engine = SternmanEngine(last_service_date, warning_light_is_on)
        self.assertFalse(Engine.needs_service())

if __name__ == "__main__":
    unittest.main()