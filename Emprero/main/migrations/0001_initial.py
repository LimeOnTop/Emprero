# Generated by Django 3.2.7 on 2022-04-22 00:41

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Category')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('photo_1', models.ImageField(upload_to='images', verbose_name='Photo 1')),
                ('photo_2', models.ImageField(upload_to='images', verbose_name='Photo 2')),
                ('photo_3', models.ImageField(upload_to='images', verbose_name='Photo 3')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('sale', models.IntegerField(verbose_name='Sale')),
                ('available', models.BooleanField(default=False, verbose_name='Available')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.categories', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Cloth',
                'verbose_name_plural': 'Clothes',
                'ordering': ['title', 'price'],
            },
        ),
        migrations.CreateModel(
            name='ClothesSizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cloth', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.clothes', verbose_name='Cloth_id')),
            ],
        ),
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Size')),
                ('clothes', models.ManyToManyField(related_name='size', through='main.ClothesSizes', to='main.Clothes')),
            ],
            options={
                'verbose_name': 'Size',
                'verbose_name_plural': 'Sizes',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='clothessizes',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.sizes', verbose_name='Size_id'),
        ),
    ]
