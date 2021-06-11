from django.test import TestCase
from subscriptions.models import Subscription
from datetime import datetime


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name="Victor",
            cpf="12345678901",
            email="contato@victorsantos.com",
            phone="13-99998888"
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto create_at attr."""
        self.assertIsInstance(self.obj.create_at, datetime)