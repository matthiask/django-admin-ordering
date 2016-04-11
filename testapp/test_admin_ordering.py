from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import User
from django.test import TestCase

try:
    from django.urls import reverse
except ImportError:  # pragma: no cover
    from django.core.urlresolvers import reverse


class OrderableAdminTest(TestCase):
    def login(self):
        u = User(
            username='test',
            is_active=True,
            is_staff=True,
            is_superuser=True)
        u.set_password('test')
        u.save()
        self.assertTrue(self.client.login(username='test', password='test'))

    def test_parent1(self):
        self.login()

        response = self.client.get(reverse('admin:testapp_parent1_add'))

        self.assertContains(
            response,
            '/static/admin_ordering/admin_ordering.js',
            1,
        )
        self.assertContains(
            response,
            'data-context="',
        )
        self.assertContains(
            response,
            '&quot;stacked&quot;: false',
        )
        self.assertContains(
            response,
            '&quot;tabular&quot;: true',
        )
        self.assertContains(
            response,
            '&quot;prefix&quot;: &quot;children&quot;',
        )

    def test_parent2(self):
        self.login()

        response = self.client.get(reverse('admin:testapp_parent2_add'))

        self.assertContains(
            response,
            '/static/admin_ordering/admin_ordering.js',
            1,
        )
        self.assertContains(
            response,
            'data-context="',
        )
        self.assertContains(
            response,
            '&quot;stacked&quot;: false',
        )
        self.assertContains(
            response,
            '&quot;tabular&quot;: true',
        )
        self.assertContains(
            response,
            '&quot;prefix&quot;: &quot;children&quot;',
        )

    def test_parent3(self):
        self.login()

        response = self.client.get(reverse('admin:testapp_parent3_add'))

        self.assertContains(
            response,
            '/static/admin_ordering/admin_ordering.js',
            1,
        )
        self.assertContains(
            response,
            'data-context="',
        )
        self.assertContains(
            response,
            '&quot;stacked&quot;: false',
        )
        self.assertContains(
            response,
            '&quot;tabular&quot;: true',
        )
        self.assertContains(
            response,
            '&quot;prefix&quot;: &quot;child3_set&quot;',
        )

    def test_parent4(self):
        self.login()

        self.client.post(reverse('admin:testapp_parent4_add'), {
            'title': 'bla',
            '_orderaaaaa': 42,
        })

        response = self.client.get(reverse('admin:testapp_parent4_changelist'))

        self.assertContains(
            response,
            '/static/admin_ordering/admin_ordering.js',
            1,
        )
        self.assertContains(
            response,
            'value="42"',
        )
        self.assertNotContains(
            response,
            '&quot;prefix&quot;: ',
        )
        self.assertContains(
            response,
            'data-context="{&quot;field&quot;: &quot;_orderaaaaa&quot;}"',
        )
