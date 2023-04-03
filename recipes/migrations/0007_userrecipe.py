# Generated by Django 4.1.7 on 2023-04-03 21:06

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0006_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_id', models.CharField(max_length=50)),
                ('recipe_name', models.CharField(max_length=250)),
                ('recipe_description', models.TextField(blank=True, null=True)),
                ('recipe_instructions', models.TextField(blank=True, null=True)),
                ('recipe_alcoholic', models.BooleanField()),
                ('recipe_db_type', models.CharField(max_length=2)),
                ('recipe_tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, null=True, size=None)),
                ('recipe_image_url', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User - Recipe',
                'verbose_name_plural': 'User - Recipes',
                'unique_together': {('user', 'recipe_id', 'recipe_db_type')},
            },
        ),
    ]