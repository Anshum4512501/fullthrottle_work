# Generated by Django 3.1 on 2020-08-08 11:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('memberactivityapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=10, primary_key=True, serialize=False),
        ),
    ]
