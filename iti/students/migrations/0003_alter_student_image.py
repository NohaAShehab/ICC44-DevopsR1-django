# Generated by Django 4.2.4 on 2023-08-22 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
