# Generated by Django 3.0.6 on 2020-05-14 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_postitem_roast'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postitem',
            old_name='boast',
            new_name='boast_or_roast',
        ),
        migrations.RemoveField(
            model_name='postitem',
            name='roast',
        ),
    ]
