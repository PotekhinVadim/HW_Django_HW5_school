# Generated by Django 4.2.7 on 2023-11-22 19:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0002_alter_student_group_alter_student_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="teacher",
        ),
        migrations.AddField(
            model_name="student",
            name="teacher",
            field=models.ManyToManyField(related_name="students", to="school.teacher"),
        ),
    ]
