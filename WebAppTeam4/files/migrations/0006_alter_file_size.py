# Generated by Django 4.2.4 on 2023-09-10 17:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('files', '0005_file_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='size',
            field=models.CharField(default='2Кб'),
        ),
    ]