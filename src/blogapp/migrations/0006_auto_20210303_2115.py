# Generated by Django 2.2 on 2021-03-03 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_auto_20210303_2108'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publishedDate', '-timeStamp', '-updated']},
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='Updated',
            new_name='updated',
        ),
    ]
