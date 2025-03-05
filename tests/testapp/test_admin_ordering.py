from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from testapp.models import Orderable


class OrderableAdminTest(TestCase):
    def login(self):
        u = User(username="test", is_active=True, is_staff=True, is_superuser=True)
        u.set_password("test")
        u.save()
        self.assertTrue(self.client.login(username="test", password="test"))

    def test_parent1(self):
        self.login()

        response = self.client.get(reverse("admin:testapp_parent1_add"))

        self.assertContains(response, "/static/admin_ordering/admin_ordering.js", 1)
        self.assertContains(response, '"stacked": false')
        self.assertContains(response, '"tabular": true')
        self.assertContains(response, '"prefix": "children"')

    def test_parent2(self):
        self.login()

        response = self.client.get(reverse("admin:testapp_parent2_add"))

        self.assertContains(response, "/static/admin_ordering/admin_ordering.js", 1)
        self.assertContains(response, '"stacked": false')
        self.assertContains(response, '"tabular": true')
        self.assertContains(response, '"prefix": "children"')

    def test_parent3(self):
        self.login()

        response = self.client.get(reverse("admin:testapp_parent3_add"))

        self.assertContains(response, "/static/admin_ordering/admin_ordering.js", 1)
        self.assertContains(response, '"stacked": false')
        self.assertContains(response, '"tabular": true')
        self.assertContains(response, '"prefix": "child3_set"')
        self.assertContains(response, '"prefix": "child3_set-2"')

    def test_parent4(self):
        self.login()

        self.client.post(
            reverse("admin:testapp_parent4_add"), {"title": "bla", "_orderaaaaa": 42}
        )

        response = self.client.get(reverse("admin:testapp_parent4_changelist"))

        self.assertContains(response, "/static/admin_ordering/admin_ordering.js", 1)
        self.assertContains(response, 'value="42"')
        self.assertNotContains(response, '"prefix": ')
        self.assertContains(response, '"field": "_orderaaaaa"')
        self.assertContains(response, '"fieldHideInput": false')

    def test_orderable_model(self):
        obj = Orderable.objects.create()
        self.assertEqual(obj.ordering, 10)

        obj = Orderable.objects.create()
        self.assertEqual(obj.ordering, 20)

        Orderable.objects.create(ordering=42)
        obj = Orderable.objects.create()
        self.assertEqual(obj.ordering, 52)
