# Generated by Django 5.2.1 on 2025-06-25 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0004_alter_cart_create_ate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='create_ate',
        ),
        migrations.AddField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
