# Generated by Django 2.1 on 2018-09-27 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfc', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-posted_on']},
        ),
    ]
