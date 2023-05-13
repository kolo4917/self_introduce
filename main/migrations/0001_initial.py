# Generated by Django 4.2 on 2023-05-13 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='이름')),
                ('usercode', models.CharField(max_length=128, verbose_name='학번')),
                ('userclass', models.CharField(max_length=128, verbose_name='과목')),
                ('usergrade', models.CharField(max_length=64, verbose_name='학점')),
                ('registered_dttm', models.DateField(auto_now_add=True, verbose_name='등록시간')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
                'db_table': 'users',
            },
        ),
    ]
