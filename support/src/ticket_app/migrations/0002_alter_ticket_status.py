# Generated by Django 3.2.8 on 2021-10-28 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.IntegerField(choices=[(0, 'Open'), (1, 'Closed'), (2, 'Freezed')], default=0),
        ),
    ]
