# Generated by Django 2.2 on 2021-03-03 21:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_blogpost_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='Updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='publishedDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
