# Generated by Django 5.2.3 on 2025-06-15 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('author_name', models.CharField(max_length=255)),
                ('author_link', models.CharField(max_length=500)),
            ],
        ),
    ]
