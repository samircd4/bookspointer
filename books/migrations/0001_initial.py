# Generated by Django 5.2.3 on 2025-06-15 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('token', models.CharField(blank=True, max_length=1000, null=True)),
                ('has_profile_image', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('reviewed_by_shraiya', models.BooleanField(default=False)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('author_id', models.IntegerField()),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('category_id', models.IntegerField()),
                ('is_posted', models.BooleanField(default=False)),
                ('book_link', models.CharField(max_length=500)),
                ('content', models.TextField()),
            ],
        ),
    ]
