# Generated by Django 3.0.6 on 2020-05-14 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200514_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='postitem',
            name='boast',
            field=models.BooleanField(default=False),
        ),
    ]