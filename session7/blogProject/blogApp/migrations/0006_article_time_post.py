# Generated by Django 4.1.7 on 2023-04-05 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0005_remove_article_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='time_post',
            field=models.DateTimeField(null=True),
        ),
    ]
