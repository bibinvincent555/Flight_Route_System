from django.db import models


class AirportRoute(models.Model):
    """
    Represents a node/stop in an ordered flight route.

    Fields:
    - airport_code: unique airport identifier
    - position: integer ordering along the route (1-based, unique)
    - duration: duration in minutes from previous node to this node
    """
    airport_code = models.CharField(max_length=10, unique=True)
    position = models.IntegerField(db_index=True, unique=True)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f"{self.airport_code} (pos {self.position}, {self.duration}m)"
