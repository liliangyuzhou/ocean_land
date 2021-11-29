# Generated by Django 3.2.8 on 2021-11-25 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('interfaces', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configures',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, help_text='逻辑删除', verbose_name='逻辑删除')),
                ('id', models.AutoField(help_text='id主键', primary_key=True, serialize=False, verbose_name='id主键')),
                ('name', models.CharField(help_text='配置名称', max_length=200, unique=True, verbose_name='配置名称')),
                ('author', models.CharField(help_text='创建人', max_length=50, verbose_name='创建人')),
                ('request', models.TextField(help_text='请求详情', verbose_name='请求详情')),
                ('interface', models.ForeignKey(help_text='所属接口', on_delete=django.db.models.deletion.CASCADE, related_name='configures', to='interfaces.interfaces')),
            ],
            options={
                'verbose_name': '测试用例配置表',
                'verbose_name_plural': '测试用例配置表',
                'db_table': 'tb_configures',
            },
        ),
    ]