from django.db import models


class Printer(models.Model):
    name = models.CharField(verbose_name='Назва принтера',
                            max_length=200,
                            unique=False,
                            )
    api_key = models.CharField(verbose_name='Ключ доступу до API',
                               max_length=250,
                               unique=True,
                               blank=False,
                               null=False, )
    check_type = models.CharField(verbose_name='Тип чека який друкує принтер',
                                  max_length=50, )
    point_id = models.IntegerField(verbose_name="Точка до якої прив'язаний принтер")

    class Meta:
        verbose_name = 'Принтер'
        verbose_name_plural = 'Принтери'


class Check(models.Model):
    printer_id = models.ForeignKey(Printer,
                                   verbose_name='Принтер',
                                   on_delete=models.CASCADE,
                                   related_name='checks', )
    defined_type = models.CharField(verbose_name='Тип чеку',
                                    max_length=50)
    order = models.JSONField(verbose_name='Інформація про замовлення')
    status = models.CharField(verbose_name='Статус чеку',
                              max_length=50
                              )
    pdf_file = models.FileField(verbose_name='PDF-файл',
                                max_length=5000,
                                upload_to='',
                                blank=True,
                                null=True,
                                )

    class Meta:
        verbose_name = 'Чек'
        verbose_name_plural = 'Чеки'
