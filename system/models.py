from django.db import models


class Category(models.Model):
    """تصنيفات الجمل"""

    name = models.CharField(max_length=100, unique=True, verbose_name='اسم التصنيف')
    image = models.ImageField(
        upload_to='category_images/',
        blank=True,
        null=True,
        verbose_name='صورة التصنيف',
    )
    order = models.IntegerField(default=0, verbose_name='الترتيب')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = 'تصنيف'
        verbose_name_plural = 'تصنيفات'

    def __str__(self):
        return self.name


class Phrase(models.Model):
    """جمل التواصل"""

    text = models.CharField(max_length=200, verbose_name='الجملة')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='phrases',
        verbose_name='التصنيف',
    )
    image = models.ImageField(
        upload_to='phrase_images/',
        blank=True,
        null=True,
        verbose_name='صورة الجملة',
    )
    audio = models.FileField(
        upload_to='phrase_audio/',
        blank=True,
        null=True,
        verbose_name='التسجيل الصوتي',
    )
    order = models.IntegerField(default=0, verbose_name='الترتيب')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاريخ التعديل')

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = 'جملة'
        verbose_name_plural = 'جمل'

    def __str__(self):
        return self.text


class Person(models.Model):
    """أشخاص العيلة"""

    name = models.CharField(max_length=100, verbose_name='الاسم')
    relation = models.CharField(max_length=100, blank=True, null=True, verbose_name='العلاقة')
    image = models.ImageField(
        upload_to='people_images/',
        blank=True,
        null=True,
        verbose_name='الصورة',
    )
    audio = models.FileField(
        upload_to='person_audio/',
        blank=True,
        null=True,
        verbose_name='التسجيل الصوتي',
    )
    order = models.IntegerField(default=0, verbose_name='الترتيب')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاريخ التعديل')

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = 'شخص'
        verbose_name_plural = 'أشخاص'

    def __str__(self):
        return f'{self.name} ({self.relation or ""})'
