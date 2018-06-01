# Generated by Django 2.0.5 on 2018-05-31 08:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_ethereum_events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonitoredEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('contract_address', models.CharField(max_length=42, validators=[django.core.validators.MinLengthValidator(42)])),
                ('topic', models.CharField(max_length=64, validators=[django.core.validators.MinLengthValidator(64)])),
                ('event_receiver', models.CharField(max_length=256)),
                ('monitored_from', models.IntegerField(blank=True, help_text='Block number in which monitoring for this event started', null=True)),
            ],
            options={
                'verbose_name_plural': 'Monitored Events',
                'verbose_name': 'Monitored Event',
            },
        ),
        migrations.AlterUniqueTogether(
            name='monitoredevent',
            unique_together={('topic', 'contract_address')},
        ),
    ]