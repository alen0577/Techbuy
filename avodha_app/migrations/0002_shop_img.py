# Generated by Django 3.2.13 on 2022-05-11 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avodha_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='images'),
            preserve_default=False,
        ),
    ]
