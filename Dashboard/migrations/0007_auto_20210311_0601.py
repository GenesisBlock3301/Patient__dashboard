# Generated by Django 3.1.7 on 2021-03-11 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0006_auto_20210310_2328'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['-id']},
        ),
    ]
