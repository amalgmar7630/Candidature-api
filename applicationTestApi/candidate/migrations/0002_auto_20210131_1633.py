# Generated by Django 3.1.5 on 2021-01-31 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='birthdate',
            field=models.DateField(db_index=True, null=True, verbose_name='Birth Date'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='firstname',
            field=models.CharField(db_index=True, max_length=30, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='lastname',
            field=models.CharField(db_index=True, max_length=30, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='years_experience',
            field=models.PositiveIntegerField(db_index=True, null=True, verbose_name='Number Years Of Experience'),
        ),
    ]