# Generated by Django 4.1.3 on 2022-11-27 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(default='email@email.com', max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='email',
            field=models.CharField(default='email@email.com', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]