# Generated by Django 4.1.3 on 2022-11-26 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_section_code_alter_section_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='code',
            field=models.CharField(max_length=7, null=True),
        ),
    ]
