from django.test import TestCase

# Create your tests here.
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
import pandas as pd

# Define this after the ModelTestCase
# class ViewTestCase(TestCase):
#     """Test suite for the api views."""

#     def setUp(self):
#         """Define the test client and other test variables."""
#         self.client = APIClient()
#         self.bucketlist_data = {'name': 'Go to Ibiza'}
#         self.response = self.client.post(
#             reverse('create'),
#             self.bucketlist_data,
#             format="json")

#     def test_api_can_create_a_bucketlist(self):
#         """Test the api has bucket creation capability."""
#         self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

class LoadRelationsCSVTest(TestCase):
    """Test suite for the api views."""
    
    def loadCSV(self):
        self.client = APIClient()
        text = pd.read_excel('/mnt/d/Projects/env/data/relations_metadata.xlsx',sheet_name='relations', header=0)
        self.relations_data = {'rel_hi':text['relation_hindi'],'rel_en':text['relation_english']}
        self.response = self.client.post(
                reverse('create'),
                self.relations_data,
                format="json")

        print(self.response)

    # print(text['relation_hindi'])
            
# LoadRelationsCSVTest.loadCSV("")
