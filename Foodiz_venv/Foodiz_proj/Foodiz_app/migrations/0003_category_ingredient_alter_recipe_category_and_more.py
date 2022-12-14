# Generated by Django 4.0.5 on 2022-08-16 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foodiz_app', '0002_rename_recipr_recipe_recipe_alter_recipe_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='ingredient',
            field=models.ManyToManyField(related_name='ingredient', to='Foodiz_app.ingredient'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.ManyToManyField(related_name='category', to='Foodiz_app.category'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredient',
            field=models.ManyToManyField(related_name='Recipe_ingredient', to='Foodiz_app.ingredient'),
        ),
    ]
