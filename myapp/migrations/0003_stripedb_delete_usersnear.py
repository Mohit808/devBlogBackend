# Generated by Django 4.0.4 on 2023-01-09 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_usersnear'),
    ]

    operations = [
        migrations.CreateModel(
            name='StripeDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=200)),
                ('userId', models.CharField(default='', max_length=100)),
                ('serviceName', models.CharField(default='', max_length=200)),
                ('amount', models.CharField(default='', max_length=200)),
            ],
            options={
                'db_table': 'StripeDb',
            },
        ),
        migrations.DeleteModel(
            name='usersNear',
        ),
    ]