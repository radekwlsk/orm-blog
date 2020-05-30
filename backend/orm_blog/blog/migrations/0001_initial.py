# Generated by Django 3.0.6 on 2020-05-30 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('website', models.URLField(blank=True, verbose_name='website')),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('posted', models.DateTimeField(blank=True, null=True, verbose_name='posted at')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('body', models.TextField(verbose_name='body')),
                ('sponsored', models.BooleanField(default=False, verbose_name='sponsored')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='views')),
                ('thumbs_up', models.PositiveIntegerField(default=0, verbose_name='thumbs up')),
                ('thumbs_down', models.PositiveIntegerField(default=0, verbose_name='thumbs down')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(max_length=2000, verbose_name='comment text')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.BlogPost')),
            ],
        ),
    ]