# Generated by Django 3.1.2 on 2020-10-14 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Blog_Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('i_images', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('category', models.ManyToManyField(to='images.Categories')),
                ('locations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.locations')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
