# Generated by Django 3.0.2 on 2020-01-29 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DruzynGaming', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(help_text='Imie', max_length=30)),
                ('nazwisko', models.CharField(help_text='Nazwisko', max_length=30)),
                ('sekcja', models.CharField(help_text='Sekcja', max_length=30)),
                ('rola', models.CharField(help_text='Rola', max_length=30)),
            ],
        ),
    ]
