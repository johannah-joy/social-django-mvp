# Generated by Django 3.0.7 on 2020-06-12 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_published']},
        ),
    ]
