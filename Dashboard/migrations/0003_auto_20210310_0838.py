# Generated by Django 3.1.7 on 2021-03-10 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0002_auto_20210310_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='patient',
            name='grade',
            field=models.CharField(default='', max_length=255),
        ),
    ]
