# Generated by Django 5.0.3 on 2024-03-05 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CRUD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=30)),
                ('Age', models.IntegerField(default='', max_length=40)),
                ('Address', models.CharField(default='', max_length=30)),
                ('Phone', models.IntegerField(default='', max_length=10)),
            ],
        ),
    ]
