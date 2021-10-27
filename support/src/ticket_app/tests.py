from django.test import TestCase
from django.contrib.auth.models import User
from message_app.models import Message
from message_app.views import MessageViewSet
from ticket_app.models import Ticket
from ticket_app.views import TicketViewSet

class TicketViewSetTestCase(TestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(username='test1', password='qqwwee112233')
        test_user1.save()

    def test_get_tickets_without_login(self):
        resp = self.client.get('/api/v1/ticket/')
        self.assertEqual(resp.status_code, 401)

    def test_create_ticket_without_title(self):
        login_resp = self.client.post('/auth/jwt/create/', {'username':'test1', 'password': 'qqwwee112233'})
        jwt = login_resp.json()['access']

        resp = self.client.post('/api/v1/ticket/', {'text': 'this is test text'}, HTTP_AUTHORIZATION='JWT ' + jwt)
        resp_data = resp.json()

        self.assertEqual(resp.status_code, 400)
        self.assertTrue('title' in resp_data)
        self.assertEqual(resp_data['title'][0], 'This field is required.')

    def test_create_ticket(self):
        login_resp = self.client.post('/auth/jwt/create/', {'username':'test1', 'password': 'qqwwee112233'})
        jwt = login_resp.json()['access']

        resp = self.client.post('/api/v1/ticket/', {'title': 'Test title', 'text': 'this is test text'}, HTTP_AUTHORIZATION='JWT ' + jwt)
        resp_data = resp.json()

        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp_data['title'], 'Test title')
        self.assertEqual(resp_data['text'], 'this is test text')
        self.assertEqual(resp_data['status'], 1)
