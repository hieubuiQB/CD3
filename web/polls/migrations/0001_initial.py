# Generated by Django 4.2.4 on 2023-08-25 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SinhVien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('adress', models.CharField(max_length=100)),
                ('grade', models.IntegerField()),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
    ]
