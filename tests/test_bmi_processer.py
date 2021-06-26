import unittest
from . import BodyMassIndex

class TestBMI(unittest.TestCase):
    def setUp(self) -> None:
        self.BMI = BodyMassIndex()
        return super().setUp()
    def test_convert_m_to_cm(self):
        self.assertEqual(self.BMI.convert_cm_to_m(height=0),0)
        self.assertEqual(self.BMI.convert_cm_to_m(height=171),1.71)
        self.assertEqual(self.BMI.convert_cm_to_m(height=300),3)
        self.assertEqual(self.BMI.convert_cm_to_m(height=1),0.01)
        self.assertEqual(self.BMI.convert_cm_to_m(height=123),1.23)

    def test_calculate_BMI(self):
        record1 = {
            "Gender":"Male",
            "HeightCm":177,
            "WeightKg":95
        }
        record1_sol = {
            "BmiCategory": "Moderately Obese",
            "HealthRisk": "Medium Risk",
            "BMI":30.32
        }
        print(self.BMI.calculate_bmi(record1))
        self.assertEqual(self.BMI.calculate_bmi(record1),record1_sol)
