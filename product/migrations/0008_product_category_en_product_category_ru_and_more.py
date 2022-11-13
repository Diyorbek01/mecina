# Generated by Django 4.1.3 on 2022-11-13 09:44

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='product.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='category_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='product.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='category_uz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='product.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_uz',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title_uz',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='comment_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='comment_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='comment_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='product_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='review',
            name='product_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='review',
            name='product_uz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]