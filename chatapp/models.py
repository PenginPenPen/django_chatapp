from django.db import models

# Create your models here.
class chat(models.Model):
    message = models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    create_at = models.DateTimeField(blank=False, null=False, auto_now_add=True)

    def __str__(self):
        return self.message