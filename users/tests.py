from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import UserProfile

class UserProfileAPITest(APITestCase):
    def setUp(self):
        # Ensuring that the database is clean before each test
        User.objects.all().delete()
        UserProfile.objects.all().delete()

        # Creating a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Using get_or_create to avoid creating a duplicate UserProfile
        self.user_profile, created = UserProfile.objects.get_or_create(
            user=self.user,
            defaults={
                'headline': 'Test Headline',
                'summary': 'Test Summary',
                'location': 'Test Location'
            }
        )

    def test_get_user_profile(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('userprofile-detail', kwargs={'pk': self.user_profile.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['headline'], 'Test Headline')

    def test_update_user_profile(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('userprofile-detail', kwargs={'pk': self.user_profile.pk})
        new_data = {
            'headline': 'Updated Headline',
            'summary': 'Updated Summary',
            'location': 'Updated Location'
        }
        response = self.client.put(url, new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user_profile.refresh_from_db()
        self.assertEqual(self.user_profile.headline, 'Updated Headline')

    def test_unauthorized_access(self):
        url = reverse('userprofile-detail', kwargs={'pk': self.user_profile.pk})
        response = self.client.put(url, {'headline': 'Unauthorized Headline'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def tearDown(self):
        # Clean up after each test
        User.objects.all().delete()
        UserProfile.objects.all().delete()
