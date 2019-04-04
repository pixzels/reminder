from django.db import models
from django.contrib.auth import authenticate, get_user_model
import uuid

User = get_user_model()


class Reminder(models.Model):
    body = models.CharField(max_length=100)
    due_date = models.DateTimeField(null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.body
