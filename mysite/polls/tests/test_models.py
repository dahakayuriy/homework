from django.test import TestCase
from polls.models import Person


class TestPerson(TestCase):
    def setUp(self):
        Person.objects.create(first_name='one', last_name='two')
        Person.objects.create(first_name='Yuriy', last_name='Murachov')

    def test_creation(self):
        person1 = Person.objects.get(first_name='one')
        person2 = Person.objects.get(first_name='Yuriy')
        self.assertEqual(person1.last_name, 'two')
        self.assertEqual(person2.last_name, 'Murachov')
