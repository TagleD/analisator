# Generated by Django 4.2 on 2025-03-25 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_transaction_risk_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
