# Generated by Django 3.1.3 on 2020-11-20 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0003_auto_20201118_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='Todo',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
