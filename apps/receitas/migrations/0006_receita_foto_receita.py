# Generated by Django 4.1 on 2022-09-06 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0005_remove_receita_data_receita_receita_date_receita_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y'),
        ),
    ]