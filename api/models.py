from django.core.validators import FileExtensionValidator
from django.db import models


class Printer(models.Model):
    """Модель принтера"""
    CHECK_TYPE = (
        ('kitchen', 'Кухня'),
        ('client', 'Клієнт'),
    )

    name = models.CharField(max_length=255,
                            verbose_name='Назва принтера')
    api_key = models.CharField(max_length=255,
                               verbose_name='ключ доступу до API'
                               )
    check_type = models.CharField(choices=CHECK_TYPE,
                                  max_length=7,
                                  default='kitchen',
                                  verbose_name='Тип чека, який друкує принтер')
    point_id = models.IntegerField(db_index=True,
                                   null=False,
                                   blank=False,
                                   verbose_name="Точки, до яких прив'язані принтери")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Принтер'
        verbose_name_plural = 'Принтери'


class Check(models.Model):
    """Модель чека"""
    CHECK_TYPE = (
        ('kitchen', 'Кухня'),
        ('client', 'Клієнт'),
    )
    STATUS = (
        ('new', 'Новий'),
        ('rendered', 'Відображений'),
        ('printed', 'Роздрукований'),
    )

    printer = models.ForeignKey(Printer,
                                on_delete=models.CASCADE,
                                related_name='check_model',
                                verbose_name='Принтер')
    type = models.CharField(choices=CHECK_TYPE,
                            max_length=7,
                            default='kitchen',
                            verbose_name='Тип чека'
                            )
    order = models.JSONField(verbose_name='Інформація про замовлення')
    status = models.CharField(choices=STATUS,
                              max_length=8,
                              default='new',
                              verbose_name='Статус чека')
    pdf_file = models.FileField(upload_to='pdf/',
                                verbose_name='Посилання на створений PDF-файл',
                                blank=True,
                                validators=[
                                    FileExtensionValidator(allowed_extensions=['pdf', ])
                                ])

    class Meta:
        verbose_name = 'Чек'
        verbose_name_plural = 'Чеки'
