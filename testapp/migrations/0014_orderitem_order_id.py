# Generated by Django 3.1.4 on 2022-01-18 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0013_delete_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='order_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]