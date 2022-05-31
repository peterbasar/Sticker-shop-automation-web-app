# Generated by Django 4.0.2 on 2022-05-08 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=508)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialOption',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='SizeLimit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=254)),
                ('minimal_side_length_mm', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('maximal_side_length_mm', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=254)),
                ('price_per_square_mm', models.DecimalField(decimal_places=4, max_digits=6)),
                ('style_icon_url', models.URLField(null=True)),
                ('style_background_image_url', models.URLField(blank=True, null=True)),
                ('size_limit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_sticker_listing.sizelimit')),
            ],
        ),
        migrations.CreateModel(
            name='StyleOption',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Sticker',
            fields=[
                ('galleryitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_sticker_listing.galleryitem')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sticker_listing.gallery')),
            ],
            bases=('app_sticker_listing.galleryitem',),
        ),
        migrations.CreateModel(
            name='StickerMaterial',
            fields=[
                ('material_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_sticker_listing.material')),
            ],
            bases=('app_sticker_listing.material',),
        ),
        migrations.CreateModel(
            name='StickerMaterialOption',
            fields=[
                ('materialoption_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_sticker_listing.materialoption')),
                ('material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_sticker_listing.stickermaterial')),
                ('sticker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sticker_listing.sticker')),
            ],
            bases=('app_sticker_listing.materialoption',),
        ),
        migrations.CreateModel(
            name='StickerStyle',
            fields=[
                ('style_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_sticker_listing.style')),
                ('sticker_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sticker_listing.stickermaterial')),
            ],
            bases=('app_sticker_listing.style',),
        ),
        migrations.CreateModel(
            name='StickerTag',
            fields=[
                ('tag_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_sticker_listing.tag')),
            ],
            bases=('app_sticker_listing.tag',),
        ),
        migrations.CreateModel(
            name='StickerStyleOption',
            fields=[
                ('styleoption_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_sticker_listing.styleoption')),
                ('img_url', models.URLField()),
                ('img_combi_url', models.URLField()),
                ('crop_img_url', models.URLField()),
                ('auto_img_width', models.IntegerField(default=0)),
                ('auto_img_height', models.IntegerField(default=0)),
                ('auto_img_aspect_ratio_w_h', models.DecimalField(decimal_places=3, default=0, max_digits=5)),
                ('auto_current_area_to_square_area_ratio', models.DecimalField(decimal_places=3, default=0, max_digits=5)),
                ('material_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sticker_listing.stickermaterialoption')),
                ('style', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_sticker_listing.stickerstyle')),
            ],
            bases=('app_sticker_listing.styleoption',),
        ),
        migrations.AddField(
            model_name='sticker',
            name='tags',
            field=models.ManyToManyField(blank=True, to='app_sticker_listing.StickerTag'),
        ),
    ]
