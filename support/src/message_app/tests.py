from django.test import TestCase
from django.contrib.auth.models import User


class MessageViewSetTestCase(TestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(username='test1', password='qqwwee112233')
        test_user1.save()

        test_user2 = User.objects.create_user(username='test2', password='qqwwee112233')
        test_user2.save()

    def test_create_message_in_own_ticket(self):
        login_resp = self.client.post('/auth/jwt/create/', {'username': 'test1', 'password': 'qqwwee112233'})
        jwt = login_resp.json()['access']

        resp = self.client.post(
            '/api/v1/ticket/', 
            {'title': 'Test title', 'text': 'this is test text'}, 
            HTTP_AUTHORIZATION='JWT ' + jwt
        )
        resp_data = resp.json()

        ticket_id = int(resp_data['id'])

        resp = self.client.post(
            '/api/v1/message/', 
            {'ticket': ticket_id, 'text': 'test message'}, 
            HTTP_AUTHORIZATION='JWT ' + jwt
        )
        resp_data = resp.json()

        self.assertTrue('ticket' in resp_data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(int(resp_data['ticket']), ticket_id)
        self.assertEqual(resp_data['text'], 'test message')

    def test_create_message_in_not_own_ticket(self):
        login_resp = self.client.post('/auth/jwt/create/', {'username': 'test1', 'password': 'qqwwee112233'})
        jwt = login_resp.json()['access']

        resp = self.client.post(
            '/api/v1/ticket/', 
            {'title': 'Test title', 'text': 'this is test text'}, 
            HTTP_AUTHORIZATION='JWT ' + jwt
        )
        resp_data = resp.json()

        ticket_id = int(resp_data['id'])

        login_resp = self.client.post('/auth/jwt/create/', {'username': 'test2', 'password': 'qqwwee112233'})
        jwt = login_resp.json()['access']

        resp = self.client.post(
            '/api/v1/message/', 
            {'ticket': ticket_id, 'text': 'test message'}, 
            HTTP_AUTHORIZATION='JWT ' + jwt
        )
        resp_data = resp.json()

        self.assertTrue('ticket' in resp_data)
        self.assertEqual(resp_data['ticket'][0], 'Messages in this ticket can be left only by a ticket author!')
