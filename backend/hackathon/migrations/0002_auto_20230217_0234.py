# Generated by Django 3.2.18 on 2023-02-17 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voice',
            name='voice_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='voice',
            name='voice_id',
            field=models.CharField(max_length=15),
        ),
    ]