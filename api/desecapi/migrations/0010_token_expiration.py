# Generated by Django 3.1.3 on 2020-11-19 09:55

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desecapi', '0009_token_allowed_subnets'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='max_age',
            field=models.DurationField(default=None, null=True, validators=[django.core.validators.MinValueValidator(datetime.timedelta(0))]),
        ),
        migrations.AddField(
            model_name='token',
            name='max_unused_period',
            field=models.DurationField(default=None, null=True, validators=[django.core.validators.MinValueValidator(datetime.timedelta(0))]),
        ),
    ]
