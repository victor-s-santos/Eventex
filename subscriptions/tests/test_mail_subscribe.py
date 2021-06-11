from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Victor Santos', cpf='12345678901',
                email='victorsantos.py@gmail.com', phone='13-99999-8888')
        self.response = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]


    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@victorsantos.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@victorsantos.com.br', 'victorsantos.py@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [ 
            'Victor Santos',
            '12345678901',
            'victorsantos.py@gmail.com',
            '13-99999-8888'

        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)