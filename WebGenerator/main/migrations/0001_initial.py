# Generated by Django 4.2.2 on 2023-06-28 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(max_length=30, verbose_name='Keywords')),
                ('location', models.CharField(max_length=30, verbose_name='Location')),
            ],
        ),
    ]
