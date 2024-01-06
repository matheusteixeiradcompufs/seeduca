from django.urls import reverse
from rest_framework import status

from pessoas.tests.test_base_pessoas import PessoaMixin, PessoasTestBase


class APIPessoaMixin(PessoaMixin):
    def list_base(self, basename):
        url = reverse(basename)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def create_base(self, data, basename):
        url = reverse(basename)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def retrieve_base(self, instance_id, basename):
        url = reverse(basename, args=[instance_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def update_base(self, instance_id, data, basename):
        url = reverse(basename, args=[instance_id])
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def destroy_base(self, instance_id, basename):
        url = reverse(basename, args=[instance_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PessoasAPITestBase(PessoasTestBase, APIPessoaMixin):
    def setUp(self) -> None:
        return super(PessoasAPITestBase, self).setUp()
