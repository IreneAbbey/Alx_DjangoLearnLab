# Generated by Django 4.2.11 on 2025-02-16 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='Unknown', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(default='Unknown', max_length=200),
            preserve_default=False,
        ),
    ]
