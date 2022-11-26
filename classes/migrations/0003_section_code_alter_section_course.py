# Generated by Django 4.1.3 on 2022-11-26 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_alter_section_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='code',
            field=models.CharField(default='abcdefg', max_length=7),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='section',
            name='course',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='classes.course'),
        ),
    ]