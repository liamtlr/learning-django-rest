from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from .models import BucketList

# Create your tests here.

class BucketListTestCase(TestCase):
    """Test Behaviours of BucketList object"""

    def setUp(self):
        """Create base conditions for tests"""
        self.bucketlist_name = "Get good at the MOFOing DRF"
        self.user = User.objects.create(username="nerd")
        self.bucketlist = BucketList(name=self.bucketlist_name, user=self.user)

    def test_bucketlist_can_save(self):
        """ Test bucketlists can be saved """
        self.old_count = BucketList.objects.count()
        self.bucketlist.save()
        self.new_count = BucketList.objects.count()
        self.assertNotEqual(self.old_count, self.new_count)

class BucketListViewsTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="nerd")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.data = {'name': 'Not be rubbish'}
        self.response = self.client.post(reverse('create'),
                                         self.data,
                                         format='json',
                                         owner=self.user.id)

    def test_api_can_create_a_bucketlist(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_bucketlist(self):
        self.bl = BucketList.objects.get()
        self.response = self.client.get(reverse('details', kwargs={'pk': self.bl.id}),format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertContains(self.response, self.bl)

    def test_api_can_update_bucketlist(self):
        """Test the api can update a given bucketlist."""
        bucketlist = BucketList.objects.get()
        change_bucketlist = {'name': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': bucketlist.id}),
            change_bucketlist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
            """Test the api can delete a bucketlist."""
            bucketlist = BucketList.objects.get()
            response = self.client.delete(
                reverse('details', kwargs={'pk': bucketlist.id}),
                format='json',
                follow=True)

            self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
