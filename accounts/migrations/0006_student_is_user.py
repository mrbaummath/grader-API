# Generated by Django 4.1.3 on 2022-12-01 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_student_email_teacher_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_user',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
