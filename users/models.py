from django.db import models
from django.contrib.auth.models import User

class OneIDProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="oneid_profile")
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    surname = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)

    birth_date = models.DateField(blank=True, null=True)
    ctzn = models.CharField(max_length=255, blank=True, null=True)
    per_adr = models.CharField(max_length=255, blank=True, null=True)
    tin = models.CharField(max_length=9, blank=True, null=True)
    pport_issue_place = models.CharField(max_length=255, blank=True, null=True)
    gd = models.IntegerField(blank=True, null=True)
    natn = models.CharField(max_length=255, blank=True, null=True)
    pport_issue_date = models.DateField(blank=True, null=True)
    pport_expr_date = models.DateField(blank=True, null=True)
    pport_no = models.CharField(max_length=255, blank=True, null=True)
    pin = models.CharField(max_length=14, blank=True, null=True)
    mob_phone_no = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    birth_place = models.CharField(max_length=255, blank=True, null=True)
    mid_name = models.CharField(max_length=255, blank=True, null=True)
    user_type = models.CharField(max_length=1, blank=True, null=True)
    sess_id = models.CharField(max_length=255, blank=True, null=True)
    ret_cd = models.IntegerField(blank=True, null=True)
    valid = models.BooleanField(default=False)
    access_token = models.CharField(max_length=255, blank=True, null=True)
    refresh_token = models.CharField(max_length=255, blank=True, null=True)
    identity_common = models.CharField(max_length=255, blank=True, null=True)
    access_token_expire_date = models.DateTimeField(null=True)

    class Meta:
        indexes = [
            models.Index(fields=['user']),
        ]
