from django.conf import settings
from django.db import models

class Sembadaapi(models.Model):
    users_id            = models.IntegerField(primary_key=True)
    user_fullname       = models.CharField(max_length=100)
    access_token        = models.CharField(max_length=100)
    access_token_secret = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "md_users"

    def __str__(self):
        return self.users_id