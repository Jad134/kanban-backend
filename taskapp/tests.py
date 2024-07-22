from django.test import TestCase


class TaskListTest(TestCase):
    def test_Task_list(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

class LoginViewTest(TestCase):
    def setUp(self):
        User = get_user_model()
        # Erstellen Sie einen Testbenutzer
        self.user = User.objects.create_user(username='temporary', email='temporary@gmail.com', password='temporary')
        # Erstellen Sie ein Token für den Testbenutzer
        self.token, _ = Token.objects.get_or_create(user=self.user)
        # Verwenden Sie APIClient zum Testen der REST-API
        self.client = APIClient()

    def test_login(self):
        # Daten für die Authentifizierungsanforderung
        data = {
            'username': 'temporary',
            'password': 'temporary'
        }
        # Senden Sie die POST-Anfrage an den Login-Endpunkt
        response = self.client.post('/login/', data, format='json')
        # Überprüfen Sie, ob die Antwort erfolgreich war
        self.assertEqual(response.status_code, 200)
        # Überprüfen Sie, ob der Token und die Benutzer-ID in der Antwort enthalten sind
        self.assertIn('token', response.data)
        self.assertIn('user_id', response.data)
        # Überprüfen Sie, ob der Token dem Benutzer zugeordnet ist
        self.assertEqual(response.data['user_id'], self.user.pk)
        self.assertEqual(response.data['token'], self.token.key)
