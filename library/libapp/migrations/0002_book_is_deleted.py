# Generated by Django 4.1.3 on 2022-12-07 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_deleted',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
