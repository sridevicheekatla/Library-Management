# Generated by Django 2.2.12 on 2022-06-06 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0010_issue_book_request_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_count',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='issue_book',
        ),
    ]
