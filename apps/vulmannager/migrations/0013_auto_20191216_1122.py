# Generated by Django 2.2.6 on 2019-12-16 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vulmannager', '0012_auto_20191216_1113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vulworkflow',
            old_name='transactor',
            new_name='transactors',
        ),
    ]