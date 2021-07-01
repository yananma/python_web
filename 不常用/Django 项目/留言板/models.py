from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField('姓名', max_length=200)
    email = models.EmailField('邮箱')
    content = models.TextField('内容', max_length=500)
    SUGGEST = 'suggest'
    CATEGORY_ITEM = (
        ('SUGGEST', 'suggest'),
        ('VERYGOOD', 'verygood'),
    )
    category = models.CharField(max_length=20, choices=CATEGORY_ITEM, default=SUGGEST)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '留言板'
        verbose_name_plural = verbose_name 

