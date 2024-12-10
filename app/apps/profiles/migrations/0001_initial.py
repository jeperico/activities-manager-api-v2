# Generated by Django 5.1 on 2024-12-10 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the user', max_length=100, verbose_name='Name')),
                ('password', models.CharField(help_text='Password of the user', max_length=100, verbose_name='Password')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created At', verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Updated At', verbose_name='Updated At')),
            ],
        ),
    ]