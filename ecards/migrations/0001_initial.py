# Generated by Django 3.2.7 on 2021-10-19 01:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CardData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='merry christmas & happy new year', max_length=200)),
                ('greet', models.TextField(default='We would like to wish all our valuable customers a Merry Christmas and Happy New Year and Holiday Season!')),
                ('promotion', models.CharField(default='up to 30% off', max_length=80)),
                ('closing_statement', models.TextField(default='We will be closed for the Christmas Season From 24th December to the 2nd January')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
