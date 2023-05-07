# Generated by Django 4.1.5 on 2023-05-07 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default=None, max_length=20)),
                ('phone_number', models.IntegerField(default=None, max_length=12, unique=True)),
                ('Email', models.EmailField(default=None, max_length=100, unique=True)),
                ('address', models.TextField(default=None, max_length=250)),
                ('department', models.CharField(choices=[('savings', 'Savings Account'), ('current', 'Current Account')], default=None, max_length=50)),
                ('materials', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
