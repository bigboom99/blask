# Generated by Django 2.2.4 on 2019-11-12 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0004_auto_20191112_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='pred_del',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]