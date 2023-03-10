# Generated by Django 4.1.3 on 2022-12-28 20:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0005_book_uid_alter_book_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_link',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='book',
            name='uname',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
