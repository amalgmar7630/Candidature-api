# Generated by Django 3.1.5 on 2021-01-31 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(db_index=True, max_length=30, verbose_name='FirstName')),
                ('lastname', models.CharField(db_index=True, max_length=30, verbose_name='Lastname')),
                ('email', models.CharField(db_index=True, max_length=200, verbose_name='Email')),
                ('birthdate', models.DateField(db_index=True, null=True, verbose_name='BirthDate')),
                ('phone', models.CharField(db_index=True, max_length=8, null=True, unique=True, verbose_name='Phone Number')),
                ('availability', models.PositiveIntegerField(db_index=True, null=True, verbose_name='Availability')),
                ('years_experience', models.PositiveIntegerField(db_index=True, null=True, verbose_name='Years Of Experience')),
                ('cv_file', models.FileField(upload_to='attachments/', verbose_name='Cv File')),
                ('message', models.TextField(blank=True, db_index=True, null=True, verbose_name='Message')),
            ],
        ),
    ]
