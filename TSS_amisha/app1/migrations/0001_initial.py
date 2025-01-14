# Generated by Django 5.0.6 on 2024-05-30 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Email', models.EmailField(max_length=254)),
                ('Photo', models.ImageField(upload_to='')),
                ('Contact', models.IntegerField()),
                ('Password', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Employee',
                'db_table': 'Employee',
            },
        ),
    ]
