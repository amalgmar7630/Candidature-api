# Generated by Django 3.1.5 on 2021-01-31 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0002_auto_20210131_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='status_email',
            field=models.CharField(blank=True, db_index=True, max_length=30, null=True, verbose_name='Status Email'),
        ),
    ]
