# Generated by Django 5.0.1 on 2024-02-03 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('rating', models.FloatField()),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]
