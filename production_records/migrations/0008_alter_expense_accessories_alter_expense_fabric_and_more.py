# Generated by Django 4.2.7 on 2023-11-21 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production_records', '0007_expense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='accessories',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='expense',
            name='fabric',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='expense',
            name='other',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='expense',
            name='sewing',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='expense',
            name='threads',
            field=models.IntegerField(),
        ),
    ]