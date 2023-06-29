# Generated by Django 4.2.1 on 2023-06-29 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.IntegerField()),
                ('parent_category_id', models.IntegerField()),
                ('category_name', models.CharField(max_length=120)),
                ('product_Categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product_categories')),
            ],
        ),
    ]
