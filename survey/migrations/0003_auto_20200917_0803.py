# Generated by Django 3.1 on 2020-09-17 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20200915_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='end_questionnaire',
            name='ccc_number',
        ),
        migrations.RemoveField(
            model_name='end_questionnaire',
            name='firstname',
        ),
        migrations.AddField(
            model_name='end_questionnaire',
            name='session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='survey.started_questionnaire'),
        ),
        migrations.AlterField(
            model_name='end_questionnaire',
            name='questionnaire',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='survey.questionnaire'),
        ),
    ]
