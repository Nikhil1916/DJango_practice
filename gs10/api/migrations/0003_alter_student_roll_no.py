# Generated by Django 4.2.6 on 2023-12-14 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_student_roll_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(),
        ),
    ]