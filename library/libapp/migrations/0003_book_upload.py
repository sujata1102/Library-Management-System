# Generated by Django 4.1.3 on 2022-12-27 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0002_book_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='upload',
            field=models.FileField(default=0, upload_to='media'),
            preserve_default=False,
        ),
    ]
