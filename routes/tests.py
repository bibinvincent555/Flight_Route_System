from django.test import TestCase
from routes.models import AirportRoute


class RouteTests(TestCase):
    def setUp(self):
        AirportRoute.objects.create(airport_code='AAA', position=1, duration=10)
        AirportRoute.objects.create(airport_code='BBB', position=2, duration=5)
        AirportRoute.objects.create(airport_code='CCC', position=3, duration=20)

    def test_find_nth_right(self):
        start = AirportRoute.objects.get(airport_code='AAA')
        target = AirportRoute.objects.get(position=start.position + 2)
        self.assertEqual(target.airport_code, 'CCC')

    def test_longest(self):
        node = AirportRoute.objects.order_by('-duration').first()
        self.assertEqual(node.airport_code, 'CCC')

    def test_shortest_between(self):
        a = AirportRoute.objects.get(airport_code='AAA')
        b = AirportRoute.objects.get(airport_code='CCC')
        lo = min(a.position, b.position)
        hi = max(a.position, b.position)
        shortest = AirportRoute.objects.filter(position__gte=lo, position__lte=hi).order_by('duration').first()
        self.assertEqual(shortest.airport_code, 'BBB')
