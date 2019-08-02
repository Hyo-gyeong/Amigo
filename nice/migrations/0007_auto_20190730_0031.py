# Generated by Django 2.2.3 on 2019-07-29 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nice', '0006_sf_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lf_comment',
            name='lforeigner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lfcomment', to='nice.Lforeigner'),
        ),
        migrations.AlterField(
            model_name='sf_comment',
            name='sforeigner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sfcomment', to='nice.Sforeigner'),
        ),
    ]
