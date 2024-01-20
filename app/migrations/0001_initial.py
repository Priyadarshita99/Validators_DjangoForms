# Generated by Django 5.0.1 on 2024-01-09 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sname', models.CharField(max_length=50)),
                ('Sprincipal', models.CharField(max_length=50)),
                ('Slocation', models.CharField(max_length=50)),
                ('email', models.EmailField(default='abc@gmail.com', max_length=254)),
                ('re_enteremail', models.EmailField(default='abc@gmail.com', max_length=254)),
            ],
        ),
    ]