# Generated by Django 3.2.4 on 2021-07-05 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0003_auto_20210630_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, null=True, upload_to='articles/'),
        ),
    ]