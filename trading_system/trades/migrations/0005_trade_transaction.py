# Generated by Django 3.1 on 2020-08-31 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0004_auto_20200831_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='transaction',
            field=models.CharField(choices=[('', ''), ('BUY', 'Buy'), ('SELL', 'Sell')], default='', max_length=10, verbose_name='Transaction'),
        ),
    ]
