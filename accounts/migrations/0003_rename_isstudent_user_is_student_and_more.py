# Generated by Django 4.1.3 on 2022-11-22 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_student_user_alter_teacher_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='isStudent',
            new_name='is_student',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='isTeacher',
            new_name='is_teacher',
        ),
        migrations.RemoveField(
            model_name='student',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='student',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to=settings.AUTH_USER_MODEL),
        ),
    ]