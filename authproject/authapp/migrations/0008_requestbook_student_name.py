# Generated by Django 2.2.12 on 2022-06-04 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_issuebook'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestbook',
            name='student_name',
            field=models.CharField(default='abcd', max_length=50),
        ),
    ]