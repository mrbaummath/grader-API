# Generated by Django 4.1.3 on 2022-11-23 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_isstudent_user_is_student_and_more'),
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='classes', to='accounts.student'),
        ),
    ]
