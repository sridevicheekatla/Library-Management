# Generated by Django 2.2.12 on 2022-06-03 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=20)),
                ('published_date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='library',
        ),
    ]
