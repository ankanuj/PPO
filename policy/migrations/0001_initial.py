# Generated by Django 2.2.2 on 2019-07-12 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ecopolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_book', models.CharField(max_length=100)),
                ('img_main', models.ImageField(upload_to='policy/%y/%m/%d/')),
            ],
        ),
    ]