import os  # Terminal temizlemek için
os.system('cls||clear')


import unittest

from employee import Employee

Name:str="MSK"
Employee_ID:int=123456


class Emplloyee_Payout_Test(unittest.TestCase):
    """Test the compute_Payout method of Employee class"""

    def setUp(self) -> None:
        """Set up fixtures"""
        self.msk=Employee(name=Name,employee_id=Employee_ID)
        return super().setUp()

    def test_is_payout_float(self):
        """Is payment float?"""
        self.assertIsInstance(self.msk.compute_payout(),float)

    def test_employee_payment_no_commission_no_hours(self):
        """test_employee_payment_no_commission_no_hours"""
        self.assertAlmostEqual(self.msk.compute_payout(),1000)

    def test_employee_payment_no_commission(self):
        """test_employee_payment_no_commission"""
        self.msk.hours_worked=10
        self.assertAlmostEqual(self.msk.compute_payout(), 2000)

    def test_employee_payment_with_commission(self):
        """test_employee_payment_with_commission"""
        self.msk.hours_worked = 10
        self.msk.contracts_landed = 10
        self.assertAlmostEqual(self.msk.compute_payout(), 3000)

    def test_employee_payment_with_commission_disbled(self):
        """test_employee_payment_with_commission_disbled"""
        self.msk.hours_worked = 10
        self.msk.contracts_landed = 10
        self.msk.has_commission = False
        self.assertAlmostEqual(self.msk.compute_payout(), 2000)





if __name__=="__main__":

    unittest.main()
    



# coverage run py_test.py
# coverage report
# coverage html

    




















