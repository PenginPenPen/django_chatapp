# Generated by Django 5.1.2 on 2024-10-21 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=20)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
