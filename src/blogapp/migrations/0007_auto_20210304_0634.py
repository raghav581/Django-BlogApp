# Generated by Django 2.2 on 2021-03-04 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_auto_20210303_2115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date', '-timeStamp', '-updated']},
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='publishedDate',
            new_name='publish_date',
        ),
    ]