# Generated by Django 4.1.5 on 2023-01-24 12:46

import base.common.constant.db_table
import base.common.utils.strings
import base.common.utils.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=256, null=True)),
                ('desc', models.TextField(null=True)),
                ('file', models.FileField(upload_to=base.common.utils.strings.get_file_field_directory, validators=[base.common.utils.validators.FileSizeValidator(200)])),
                ('is_deleted', models.BooleanField(default=False)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name=base.common.constant.db_table.DBTable['FILE_MANAGEMENT'], to='master.masterfiletype')),
            ],
            options={
                'db_table': base.common.constant.db_table.DBTable['FILE_MANAGEMENT'],
            },
        ),
    ]
