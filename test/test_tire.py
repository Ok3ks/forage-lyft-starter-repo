from src.tires import CarriganTires,OctoPrimeTires
import numpy as np

import unittest
from datetime import datetime


class testCarriganTires(unittest.TestCase):
    def test_these_are_correct_readings(self):
        tires = CarriganTires(0.1,0.5,0.7,0.9)
        self.assertTrue(all(tires.sensors()) in np.arange(0,1.1, 0.1))
        self.assertTrue(type(tires.sensors()) == list)
    
    def test_these_are_incorrect_readings(self):
        tires = CarriganTires(0.1,0.5,0.7,1.3)
        self.assertTrue(all(tires.sensors()) in np.arange(0,1.1, 0.1))
        self.assertTrue(type(tires.sensors()) == list)

    def test_carrigan_tires_should_be_serviced(self):
        tires = CarriganTires(0.1,0.5,0.7,0.9)
        self.assertTrue(tires.needs_service())

    def test_carrigan_tires_should_not_be_serviced(self):
        tires = CarriganTires(0.1,0.5,0.7,0.8)
        self.assertFalse(tires.needs_service())


class testOctoPrimeTires(unittest.TestCase):
    def test_these_are_correct_readings(self):
        tires = OctoPrimeTires(0.1,0.5,0.7,0.9)
        self.assertTrue(all(tires.sensors()) in np.arange(0,1.1,0.1))
        self.assertTrue(type(tires.sensors()) == list)
    
    def test_carrigan_tires_should_be_serviced(self):
        tires = OctoPrimeTires(0.9,0.9,0.9,0.9)
        self.assertTrue(tires.needs_service())

    def test_carrigan_tires_should_not_be_serviced(self):
        tires = OctoPrimeTires(0.1,0.5,0.7,0.9)
        self.assertFalse(tires.needs_service())

