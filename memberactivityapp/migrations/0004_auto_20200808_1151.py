# Generated by Django 3.1 on 2020-08-08 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberactivityapp', '0003_auto_20200808_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='id',
            field=models.UUIDField(default='E701B9', editable=False, primary_key=True, serialize=False),
        ),
    ]
