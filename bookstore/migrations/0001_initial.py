# Generated by Django 3.2.11 on 2024-07-12 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField(max_length=60, unique=True)),
                ('image', models.ImageField(upload_to='images/books_img/')),
                ('author', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True, max_length=3000)),
                ('price', models.IntegerField()),
                ('stocks', models.IntegerField()),
                ('stocks_available', models.BooleanField(default=True)),
                ('modified_on', models.DateTimeField(auto_now_add=True)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]