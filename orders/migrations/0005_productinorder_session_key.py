# Generated by Django 4.0.4 on 2022-06-28 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinorder',
            name='session_key',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
    ]