# Generated by Django 2.2 on 2019-04-30 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20190430_1438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unit',
            old_name='deffence',
            new_name='defence',
        ),
    ]