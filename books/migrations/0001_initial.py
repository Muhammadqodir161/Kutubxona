# Generated by Django 5.1.1 on 2024-10-03 12:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('author_name', models.CharField(max_length=100)),
                ('published_at', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
