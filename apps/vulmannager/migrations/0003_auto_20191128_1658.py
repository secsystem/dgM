# Generated by Django 2.2.6 on 2019-11-28 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vulmannager', '0002_auto_20191128_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penetrationtestticket',
            name='ticket_result',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='result', to='vulmannager.PenetrationTestTicketResult'),
        ),
    ]