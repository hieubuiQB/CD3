# Generated by Django 4.0.4 on 2023-10-20 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTA', '0004_alter_course_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(),
        ),
    ]
