# Generated by Django 4.2 on 2025-03-23 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customuser_pagination_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='pagination_count',
            field=models.PositiveSmallIntegerField(choices=[(25, '25 records per page'), (50, '50 records per page'), (75, '75 records per page'), (100, '100 records per page')], default=50, verbose_name='Number of records per page'),
        ),
    ]
