# Generated by Django 3.0.5 on 2020-07-14 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('era', '0002_pdf_sname'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdf',
            name='image',
            field=models.ImageField(default='media/img/book.jpg', upload_to='media/books/img'),
        ),
    ]
