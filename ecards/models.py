from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import CharField, TextField
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import uuid
# Create your models here.


class CardData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=12, blank=True, unique=True)
    business_name = models.CharField(max_length=100, blank=True)
    title = models.CharField(
        max_length=200, default="merry christmas & happy new year")
    greet = models.TextField(
        default="We would like to wish all our valuable customers a Merry Christmas and Happy New Year and Holiday Season!")
    promotion = models.CharField(max_length=80, default="up to 30% off")
    closing_statement = models.TextField(
        default="We will be closed for the Christmas Season From 24th December to the 2nd January")
    image = models.ImageField(verbose_name="background image", blank=True, null=True)
    add_start_date = models.DateField(blank=True, null=True, verbose_name="Pop up start date")
    add_end_date = models.DateField(blank=True, null=True, verbose_name="Pop up end date")
    is_popup_active = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

@receiver(pre_save, sender=CardData)
def pre_save_create_ref_code(sender, instance, *args, **kwargs):
    if instance.ref_code == "":
        instance.ref_code = str(uuid.uuid4()).replace("-", "").upper()[:12]