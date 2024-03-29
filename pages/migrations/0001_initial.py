# Generated by Django 2.2.3 on 2019-07-12 16:31

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPageClients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about_images', verbose_name='О нас - Изображения секция 2')),
                ('is_active', models.BooleanField(default=True, verbose_name='Показывать на странице?')),
            ],
            options={
                'verbose_name': 'Избражение клиента',
                'verbose_name_plural': 'Избражения клиентов',
            },
        ),
        migrations.CreateModel(
            name='AboutPageWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about_images', verbose_name='О нас - Изображения секция 3')),
                ('is_active', models.BooleanField(default=True, verbose_name='Показывать на странице?')),
            ],
            options={
                'verbose_name': 'Избражение продукции',
                'verbose_name_plural': 'Избражения продукции',
            },
        ),
        migrations.CreateModel(
            name='AboutSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about_images', verbose_name='О нас - Изображения для слайдера')),
                ('is_active', models.BooleanField(default=True, verbose_name='Показывать на странице?')),
            ],
            options={
                'verbose_name': 'Избражение в слайдер',
                'verbose_name_plural': 'Избражения в слайдере',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='НАШИ КЛИЕНТЫ', max_length=30, verbose_name='Название категории')),
                ('name_slug', models.CharField(blank=True, max_length=30)),
                ('image', models.ImageField(upload_to='category_images', verbose_name='Картинка категории')),
                ('is_active', models.BooleanField(default=True, verbose_name='Показывать на странице?')),
                ('views', models.IntegerField(default=0, verbose_name='Просмотров категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Forms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Нет данных', max_length=255, verbose_name='Поле - Ваше имя')),
                ('phone', models.CharField(blank=True, default='Нет данных', max_length=255, verbose_name='Поле - Телефон')),
                ('email', models.CharField(blank=True, default='Нет данных', max_length=255, verbose_name='Поле - Email')),
                ('file', models.FileField(blank=True, upload_to='form_files', verbose_name='Загруженный файл')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30, verbose_name='Название товара')),
                ('name_slug', models.CharField(blank=True, max_length=30)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='Описание товара')),
                ('min_order', models.IntegerField(default=0, verbose_name='Минимальный заказ')),
                ('min_price', models.IntegerField(default=0, verbose_name='Минимальная стоимость')),
                ('max_price', models.IntegerField(default=0, verbose_name='Максимальная стоимость')),
                ('is_active', models.BooleanField(default=True, verbose_name='Показывать на странице?')),
                ('views', models.IntegerField(default=0, verbose_name='Просмотров товара')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pages.Category', verbose_name='Товар в категории')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_header_section1', models.CharField(default='О НАС', max_length=30, verbose_name='О нас - Заголовок секция 1')),
                ('about_text1_section1', ckeditor_uploader.fields.RichTextUploadingField(default='Текст 1 секция 1', verbose_name='О нас - Текст 1 секция 1')),
                ('about_text2_section1', ckeditor_uploader.fields.RichTextUploadingField(default='Текст 2 секция 1', verbose_name='О нас - Текст 2 секция 1')),
                ('about_header_section2', models.CharField(default='НАШИ КЛИЕНТЫ', max_length=30, verbose_name='О нас - Заголовок секция 1')),
                ('about_text1_section2', ckeditor_uploader.fields.RichTextUploadingField(default='Текст 1 секция 2', verbose_name='О нас - Текст 1 секция 2')),
                ('about_header_section3', models.CharField(default='НАШЕ ПРОИЗВОДСТВО', max_length=30, verbose_name='О нас - Заголовок секция 3')),
                ('about_title', models.CharField(default='О НАС', max_length=30, verbose_name='О нас - Title страницы')),
                ('about_descripton', models.CharField(default='О НАС', max_length=30, verbose_name='О нас - Descripton страницы')),
                ('about_keywords', models.CharField(default='О НАС', max_length=30, verbose_name='О нас - Keywords страницы')),
                ('contact_header_section1', models.CharField(default='КОНТАКТЫ', max_length=30, verbose_name='Контакты - Заголовок секция 1')),
                ('contact_text1_section1', ckeditor_uploader.fields.RichTextUploadingField(default='Текст 1 секция 1', verbose_name='Контакты - Текст 1 секция 1')),
                ('contact_header_section2', models.CharField(default='РЕКВИЗИТЫ', max_length=30, verbose_name='Контакты - Заголовок секция 2')),
                ('contact_text1_section2', ckeditor_uploader.fields.RichTextUploadingField(default='Текст 1 секция 2', verbose_name='Контакты - Текст 1 секция 2')),
                ('contact_image', models.ImageField(upload_to='contact', verbose_name='Контакты - Изображение в шапке')),
                ('contact_title', models.CharField(default='КОНТАКТЫ', max_length=30, verbose_name='Контакты - Title страницы')),
                ('contact_descripton', models.CharField(default='КОНТАКТЫ', max_length=30, verbose_name='Контакты - Descripton страницы')),
                ('contact_keywords', models.CharField(default='КОНТАКТЫ', max_length=30, verbose_name='Контакты - Keywords страницы')),
                ('category_main_title', models.CharField(default='Портфолио', max_length=30, verbose_name='Портфолио (Категории) - Title страницы')),
                ('category_main_descripton', models.CharField(default='Портфолио', max_length=30, verbose_name='Портфолио (Категории) - Descripton страницы')),
                ('category_main_keywords', models.CharField(default='Портфолио', max_length=30, verbose_name='Портфолио (Категории) - Keywords страницы')),
                ('category_items_title', models.CharField(default='Портфолио', max_length=30, verbose_name='Портфолио (Товары) - Title страницы')),
                ('category_items_descripton', models.CharField(default='Портфолио', max_length=30, verbose_name='Портфолио (Товары) - Descripton страницы')),
                ('category_items_keywords', models.CharField(default='Портфолио', max_length=30, verbose_name='Портфолио (Товары) - Keywords страницы')),
                ('category_item_title', models.CharField(default='Портфолио', max_length=30, verbose_name='Портфолио (Товар) - Title страницы')),
                ('category_item_descripton', models.CharField(default='Портфолио', max_length=30, verbose_name='Портфолио (Товар) - Descripton страницы')),
                ('category_item_keywords', models.CharField(default='Портфолио', max_length=30, verbose_name='Портфолио (Товар) - Keywords страницы')),
                ('services_header_section1', models.CharField(default='Услуги', max_length=30, verbose_name='Услуги - Заголовок секция 1')),
                ('services_text1_section1', ckeditor_uploader.fields.RichTextUploadingField(default='Текст 1 секция 1', verbose_name='Услуги - Текст 1 секция 1')),
                ('services_item_title', models.CharField(default='Портфолио', max_length=30, verbose_name='Услуги - Title страницы')),
                ('services_item_descripton', models.CharField(default='Портфолио', max_length=30, verbose_name='Услуги - Descripton страницы')),
                ('services_item_keywords', models.CharField(default='Портфолио', max_length=30, verbose_name='Услуги - Keywords страницы')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(default='Услуги', max_length=30, verbose_name='Услуги - Заголовок ')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='Услуги - Текст ')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='item_images', verbose_name='Изображение товара')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pages.Item', verbose_name='Изображение для товара')),
            ],
            options={
                'verbose_name': 'Изображение для товара',
                'verbose_name_plural': 'Изображения для товаров',
            },
        ),
    ]
