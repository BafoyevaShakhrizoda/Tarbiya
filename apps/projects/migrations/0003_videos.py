# Generated by Django 5.2.4 on 2025-07-25 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_banner_button_text_en_banner_button_text_kg_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('video', models.FileField(upload_to='videos/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
