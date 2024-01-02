from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate, APIClient

from lessons.models import Kurs, Subscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(email='user@test.com', password='test', username='username')
        self.client.force_authenticate(user=self.user)  # Аутентифицируем клиента с созданным пользователем

        datakurs = {'title': 'Test', }
        self.client.post('/kurs/', data=datakurs)

    def test_CRUD_lesson(self):
        data = {'title': 'Test',
                'description': 'Test',
                'video': 'www.youtube.com/jjj',
                'kurs': 1,
                'owner': 1}

        # CREATE
        response = self.client.post('/create/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {'id': 1, 'title': 'Test', 'description': 'Test', 'picture': None,
                                           'video': 'www.youtube.com/jjj', 'kurs': 1, 'owner': 1})
        self.assertTrue(Kurs.objects.all().exists())

        # UPDATE
        data2 = {'title': 'Test2', }
        response = self.client.patch('/update/1', data=data2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # GET
        response = self.client.get('/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'id': 1, 'title': 'Test2', 'description': 'Test', 'picture': None,
                                           'video': 'www.youtube.com/jjj', 'kurs': 1, 'owner': 1})

        # GET_LIST
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),  {'count': 1,
                                            'next': None,
                                            'previous': None,
                                            'results': [{'description': 'Test',
                                                         'id': 1,
                                                         'kurs': 1,
                                                         'owner': 1,
                                                         'picture': None,
                                                         'title': 'Test2',
                                                         'video': 'www.youtube.com/jjj'}]})

        # DELETE
        response = self.client.delete('/destroy/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SubscriptionTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(email='user@test.com', password='test', username='username')
        self.client.force_authenticate(user=self.user)  # Аутентифицируем клиента с созданным пользователем

        datakurs = {'title': 'Test', }
        self.client.post('/kurs/', data=datakurs)

    def test_CD_Subscription(self):

        # CREATE
        response = self.client.post('/2/subscribe/')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {'label_current_subscriptions': 'Вы уже подписаны на курсы: Test',
                                           'label': 'Вы подписываетесь на курс: ', 'kurs': 2})
        self.assertTrue(Subscription.objects.all().exists())

        # DELETE
        response = self.client.delete('/unsubscribe/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
