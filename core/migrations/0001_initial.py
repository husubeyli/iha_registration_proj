# Generated by Django 4.1.2 on 2022-12-05 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IHA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ad')),
                ('marka', models.CharField(max_length=50, verbose_name='marka')),
                ('product', models.CharField(max_length=255)),
                ('price', models.SmallIntegerField(default=0)),
                ('month', models.SmallIntegerField(default=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muddet', models.CharField(max_length=100)),
            ],
        ),
    ]
