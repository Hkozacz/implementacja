# Generated by Django 3.0.2 on 2020-01-28 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Tytuł', max_length=120)),
                ('message', models.TextField(help_text='Treść')),
            ],
        ),
    ]
