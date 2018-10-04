from django.test import TestCase, Client
from django.urls import resolve, reverse

from users.models import User
from invoice import views
from invoice.models.customer import Customer

class CustomerCreationTest(TestCase):
       # signup new user
        # - register new user
        # - check if user has been created in db and other checks
        # - login in the user
        # - post customer details
        # - check for new customer in db

    def setUp(self):
        User.objects.create_user(
            username="janedoe",
            password="janedoepass",
            email="janedoe@example.com"
        )

        self.client = Client()

    def tearDown(self):
        self.client.logout()
    
    def test_user_can_log_in(self): 
        user_login = self.client.login(username="janedoe", password="janedoepass")
        self.assertTrue(user_login, msg="User cannot login")
        
    def test_logged_in_user_can_reach_customer_creation_view(self):
       self.client.login(username="janedoe", password="janedoepass")

       response = self.client.get(reverse('invoice:new_customer'))
       self.assertTrue(response.status_code, 200)
       self.assertIn('<label class="col-sm-3 control-label">City State Zip:</label>', response.content)
       self.assertIn('<div class="panel-heading">New Customer</div>', response.content)
    
    def test_register_new_user_and_test_whether_user_is_in_db(self):
        response = self.client.post(reverse("users:registration"), {
            "username": "jojo",
            "first_name": "jojo",
            "last_name": "tom",
            "password": "7445sddw56222",
            "email": "jojo@example.com",
            "user_type": "REGULAR"
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/invoice/')

        user = User.objects.filter(username='jojo').first()

        self.assertEqual(user.username, 'jojo')
        self.assertEqual(user.email, "jojo@example.com")

    def test_logged_in_user_can_create_new_customer(self):
        self.client.login(username="janedoe", password="janedoepass")

        response = self.client.post(reverse('invoice:new_customer'), {
            'name': 'johnny',
            'address1': '784 street',
            'address2': '458 street',
            'city': 'Accra',
            'state': 'Ghana',
            'zip': '475125',
            'email': 'johnny@example.com'
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/invoice/customers/')

        customer = Customer.objects.filter(name='johnny').first()
        self.assertEqual(customer.name, 'johnny')
        self.assertEqual(customer.address1, '784 street')
        self.assertEqual(customer.email, 'johnny@example.com')
    
