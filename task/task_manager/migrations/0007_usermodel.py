# Generated by Django 2.2.4 on 2020-02-09 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0006_personmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ip', models.CharField(blank=True, max_length=200)),
                ('user_id', models.CharField(blank=True, max_length=100)),
                ('token', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]
