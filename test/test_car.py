import unittest
from datetime import datetime

from src.car import CarFactory
from src.engine import CapuletEngine, SternmanEngine, WilloughbyEngine
from src.battery import SpindlerBattery, NubbinBattery


class TestCalliope(unittest.TestCase):
    def test_car_is_calliope(self):
        current_mileage = 30_001
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        calliope_car = car.create_calliope()

        self.assertTrue(type(calliope_car.engine), CapuletEngine)
        self.assertEqual(type(calliope_car.battery), SpindlerBattery)
    
    def test_car_is_not_calliope(self):
        current_mileage = 30_001
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        calliope_car = car.create_calliope()

        self.assertTrue(type(calliope_car.engine), CapuletEngine)
        self.assertNotEqual(type(calliope_car.battery), NubbinBattery)

    def test_calliope_battery_should_be_serviced(self):
        current_mileage = 30_001
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        calliope_car = car.create_calliope()
        self.assertTrue(calliope_car.battery.needs_service())

    def test_calliope_battery_should_not_be_serviced(self):
        current_mileage = 30_001
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        calliope_car = car.create_calliope()
        self.assertFalse(calliope_car.battery.needs_service())
    
    ###
    def test_calliope_engine_should_be_serviced(self):
        current_mileage=30001
        last_service_mileage=0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        car = CarFactory(today, last_service_date, current_mileage, last_service_mileage)
        calliope_car = car.create_calliope()
        #print(calliope_car.engine.needs_service())
        self.assertTrue(calliope_car.engine.needs_service())

    def test_calliope_engine_should_not_be_serviced(self):
        current_mileage = 29_999
        last_service_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        car = CarFactory(today, last_service_date, current_mileage, last_service_mileage)
        calliope_car = car.create_calliope()
        self.assertFalse(calliope_car.engine.needs_service())

    def test_calliope_should_be_serviced(self):
        current_mileage = 30_001
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        calliope_car = car.create_calliope()        
        self.assertTrue(calliope_car.needs_service())
        
        current_mileage = 30_001
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        calliope_car = car.create_calliope()        
        self.assertTrue(calliope_car.needs_service())

        current_mileage = 29_999
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        calliope_car = car.create_calliope()        
        self.assertTrue(calliope_car.needs_service())

    def test_calliope_should_not_be_serviced(self):
        current_mileage = 29_999
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        calliope_car = car.create_calliope()
        self.assertFalse(calliope_car.needs_service())

class TestGlissade(unittest.TestCase):
    def test_car_is_glissade(self):

        current_mileage = 30_001
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        glissade_car= car.create_glissade()

        self.assertTrue(type(glissade_car.engine), WilloughbyEngine)
        self.assertEqual(type(glissade_car.battery), NubbinBattery)
    
    def test_car_is_not_glissade(self):
        current_mileage = 60_001
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        
        glissade_car = car.create_glissade()
        self.assertTrue(type(glissade_car.engine), WilloughbyEngine)
        self.assertNotEqual(type(glissade_car.battery), SpindlerBattery)

    def test_glissade_battery_should_be_serviced(self):

        current_mileage = 60_001
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        glissade_car= car.create_glissade()
        self.assertTrue(glissade_car.battery.needs_service())

    def test_glissade_battery_should_not_be_serviced(self):
        current_mileage = 60_001
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        glissade_car = car.create_glissade()
        self.assertFalse(glissade_car.battery.needs_service())
    
    def test_glissade_engine_should_be_serviced(self):
        current_mileage=60001
        last_service_mileage=0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = CarFactory(today, last_service_date, current_mileage, last_service_mileage)
        glissade_car = car.create_glissade()
        self.assertTrue(glissade_car.engine.needs_service())

    def test_glissade_engine_should_not_be_serviced(self):
        current_mileage = 59_999
        last_service_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = CarFactory(today, last_service_date, current_mileage, last_service_mileage)
        glissade_car = car.create_glissade()
        self.assertFalse(glissade_car.engine.needs_service())

    def test_glissade_should_be_serviced(self):
        current_mileage = 60_001
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        glissade_car = car.create_glissade()        
        self.assertTrue(glissade_car.needs_service())
        
        current_mileage = 60_001
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        glissade_car = car.create_glissade()        
        self.assertTrue(glissade_car.needs_service())

        current_mileage = 59_999
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        glissade_car = car.create_glissade()        
        self.assertTrue(glissade_car.needs_service())

    def test_glissade_should_not_be_serviced(self):
        current_mileage = 59_999
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        glissade_car = car.create_glissade()
        self.assertFalse(glissade_car.needs_service())

class TestThovex(unittest.TestCase):
    def test_car_is_thovex(self):

        current_mileage = 30_001
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        
        thovex_car= car.create_thovex()
        self.assertTrue(type(thovex_car.engine), CapuletEngine)
        self.assertEqual(type(thovex_car.battery), NubbinBattery)
    
    def test_car_is_not_thovex(self):
        current_mileage = 29_999
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        thovex_car = car.create_thovex()

        self.assertTrue(type(thovex_car.engine), WilloughbyEngine)
        self.assertNotEqual(type(thovex_car.battery), NubbinBattery)

    def test_thovex_battery_should_be_serviced(self):

        current_mileage = 29_999
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        thovex_car= car.create_thovex()

        self.assertTrue(thovex_car.battery.needs_service())

    def test_thovex_battery_should_not_be_serviced(self):
        current_mileage = 30_001
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        thovex_car = car.create_thovex()

        self.assertFalse(thovex_car.battery.needs_service())
    
    def test_thovex_engine_should_be_serviced(self):
        current_mileage=30_001
        last_service_mileage=0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = CarFactory(today, last_service_date, current_mileage, last_service_mileage)
        thovex_car = car.create_thovex()
        self.assertTrue(thovex_car.engine.needs_service())

    def test_rorschach_engine_should_not_be_serviced(self):
        current_mileage = 59_999
        last_service_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = CarFactory(today, last_service_date, current_mileage, last_service_mileage)
        thovex_car = car.create_thovex()
        self.assertFalse(thovex_car.engine.needs_service())

    def test_rorschach_should_be_serviced(self):
        current_mileage = 30_001
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        thovex_car = car.create_thovex()       
        self.assertTrue(thovex_car.needs_service())
        
        current_mileage = 30_001
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        thovex_car = car.create_thovex()       
        self.assertTrue(thovex_car.needs_service())

        current_mileage = 29_999
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        thovex_car = CarFactory(today, last_service_date, current_mileage, last_mileage).create_glissade()  
        self.assertTrue(thovex_car.needs_service())

    def test_thovex_should_not_be_serviced(self):
        
        current_mileage = 29_999
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        thovex_car = car.create_thovex()       
        self.assertFalse(thovex_car.needs_service())

class TestPalindrome(unittest.TestCase):
    def test_car_is_palindrome(self):
        current_mileage = 30_001
        last_mileage = 0

        warning_light_on = False

        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        palindrome_car = car.create_palindrome(warning_light_on)

        self.assertTrue(type(palindrome_car.engine), SternmanEngine)
        self.assertEqual(type(palindrome_car.battery), SpindlerBattery)
    
    def test_car_is_not_palindrome(self):
        current_mileage = 30_001
        last_mileage = 0
        warning_light_on = False
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        palindrome_car = car.create_palindrome(warning_light_on)

        self.assertTrue(type(palindrome_car.engine), CapuletEngine)
        self.assertNotEqual(type(palindrome_car.battery), NubbinBattery)

    def test_palindrome_battery_should_be_serviced(self):
        current_mileage = 30_001
        last_mileage = 0
        warning_light_on = False
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        palindrome_car = car.create_palindrome(warning_light_on)
        self.assertTrue(palindrome_car.battery.needs_service())

    def test_palindrome_battery_should_not_be_serviced(self):
        current_mileage = 30_001
        last_mileage = 0
        warning_light_on = False
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        palindrome_car = car.create_palindrome(warning_light_on)
        self.assertFalse(palindrome_car.battery.needs_service())
    
    ###
    def test_palindrome_engine_should_be_serviced(self):
        current_mileage=30001
        last_service_mileage=0
        
        warning_light_on = True
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        car = CarFactory(today, last_service_date, current_mileage, last_service_mileage)
        palindrome_car = car.create_palindrome(warning_light_on= warning_light_on)
        self.assertTrue(palindrome_car.engine.needs_service())

    def test_palindrome_engine_should_not_be_serviced(self):
        current_mileage = 29_999
        last_service_mileage = 0
        warning_light_on = False
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        car = CarFactory(today, last_service_date, current_mileage, last_service_mileage)
        palindrome_car = car.create_palindrome(warning_light_on)
        self.assertFalse(palindrome_car.engine.needs_service())

    def test_palindrome_should_be_serviced(self):
        current_mileage = 30_001
        last_mileage = 0

        warning_light_on = True
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        
        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        palindrome_car = car.create_palindrome(warning_light_on)        
        self.assertTrue(palindrome_car.needs_service())

        warning_light_on = False
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        palindrome_car = car.create_palindrome(warning_light_on)        
        self.assertTrue(palindrome_car.needs_service())

    def test_palindrome_should_not_be_serviced(self):
        current_mileage = 30_001
        warning_light_on = False

        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        last_service_mileage = 0

        car = CarFactory(last_service_date, today, current_mileage, last_service_mileage)
        palindrome_car = car.create_palindrome(warning_light_on)
        self.assertFalse(palindrome_car.needs_service())

class TestThovex(unittest.TestCase):
    def test_car_is_rorschach(self):

        current_mileage = 30_001
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        rorschach_car= car.create_rorschach()

        self.assertTrue(type(rorschach_car.engine), WilloughbyEngine)
        self.assertEqual(type(rorschach_car.battery), NubbinBattery)
    
    def test_car_is_not_rorschach(self):
        current_mileage = 60_001
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        rorschach_car = car.create_rorschach()

        self.assertTrue(type(rorschach_car.engine), WilloughbyEngine)
        self.assertNotEqual(type(rorschach_car.battery), SpindlerBattery)

    def test_rorschach_battery_should_be_serviced(self):

        current_mileage = 60_001
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        rorschach_car= car.create_rorschach()

        self.assertTrue(rorschach_car.battery.needs_service())

    def test_rorschach_battery_should_not_be_serviced(self):
        current_mileage = 60_001
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        rorschach_car = car.create_rorschach()

        self.assertFalse(rorschach_car.battery.needs_service())
    
    def test_rorschach_engine_should_be_serviced(self):
        current_mileage=60001
        last_service_mileage=0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = CarFactory(today, last_service_date, current_mileage, last_service_mileage)
        rorschach_car = car.create_rorschach()
        self.assertTrue(rorschach_car.engine.needs_service())

    def test_rorschach_engine_should_not_be_serviced(self):
        current_mileage = 59_999
        last_service_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = CarFactory(today, last_service_date, current_mileage, last_service_mileage)
        rorschach_car = car.create_rorschach()
        self.assertFalse(rorschach_car.engine.needs_service())

    def test_rorschach_should_be_serviced(self):
        current_mileage = 60_001
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        rorschach_car = car.create_rorschach()       
        self.assertTrue(rorschach_car.needs_service())
        
        current_mileage = 60_001
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        rorschach_car = car.create_rorschach()       
        self.assertTrue(rorschach_car.needs_service())

        current_mileage = 59_999
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        rorschach_car = CarFactory(today, last_service_date, current_mileage, last_mileage).create_glissade()  
        self.assertTrue(rorschach_car.needs_service())

    def test_rorschach_should_not_be_serviced(self):
        
        current_mileage = 59_999
        last_mileage = 0
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = CarFactory(today, last_service_date, current_mileage, last_mileage)
        rorschach_car = car.create_rorschach()       
        self.assertFalse(rorschach_car.needs_service())

if __name__ == '__main__':
    unittest.main()
