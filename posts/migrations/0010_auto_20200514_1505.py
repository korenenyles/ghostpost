# Generated by Django 3.0.6 on 2020-05-14 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20200514_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postitem',
            name='boast',
        ),
        migrations.RemoveField(
            model_name='postitem',
            name='roast',
        ),
        migrations.AddField(
            model_name='postitem',
            name='boastorroast',
            field=models.BooleanField(default=False, help_text='boast if clicked'),
        ),
    ]
