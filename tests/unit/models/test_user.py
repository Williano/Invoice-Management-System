from django.db.models import QuerySet
from django.test import TestCase

from users.models import User


class UserModelTest(TestCase):

    def setUp(self):
        User.objects.create(
            username="johndoe",
            password="johndoepass",
            email="johndoe@example.com"
        )

        User.objects.create(
            username="janefoe",
            password="janefoepass",
            email="janefoe@example.com"
        )

    def test_model_contain_user(self):
        user = User.objects.get(username="johndoe")

        self.assertEquals(user.__unicode__(), "johndoe")
        self.assertEquals(user.password, "johndoepass")
        self.assertEquals(user.email, "johndoe@example.com")
        self.assertIsNotNone(user)

    def test_model_contains_all_users(self):
        users = User.objects.all()
        self.assertEqual(users.count(), 2)
        self.assertIsInstance(users, QuerySet)

    def test_can_delete_record(self):
        val = User.objects.get(username="janefoe").delete()

        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(val[0], 1)