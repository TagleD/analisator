# Generated by Django 4.2 on 2025-03-23 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_remove_transaction_transaction_varchar_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_varchar_id',
            field=models.CharField(default='', max_length=10, verbose_name='Уникальный сгенерированный ID транзакции'),
            preserve_default=False,
        ),
    ]
