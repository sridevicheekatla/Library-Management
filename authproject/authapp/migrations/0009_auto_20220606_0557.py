# Generated by Django 2.2.12 on 2022-06-06 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_requestbook_student_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='issueBook',
        ),
        migrations.DeleteModel(
            name='requestBook',
        ),
    ]
