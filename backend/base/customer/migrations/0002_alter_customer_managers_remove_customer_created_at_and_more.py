# Generated by Django 4.1.5 on 2023-01-25 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customer',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='is_leave',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='password',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='updated_at',
        ),
    ]
