from django.test import TestCase

# models test
from invoice.models.customer import Customer


class CustomerTest(TestCase):

    @staticmethod
    def create_customer():
        return Customer.objects.create(name="mPedigree",
                                       address1="P.O.Box KS 10731",
                                       address2="Adum",
                                       city="Kumasi",
                                       state="Ashanti",
                                       zip="00233",
                                       email="paawilly17@gmail.com",
                                       )

    def test_customer_creation(self):
        w = self.create_customer()
        self.assertTrue(isinstance(w, Customer))
        self.assertEqual(w.__str__(), w.name)
