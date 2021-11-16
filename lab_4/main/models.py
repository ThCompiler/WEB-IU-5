from django.db import models


# Create your models here.

class IcecreamManager(models.Manager):
    def get_short_des(self):
        return self.all().only('image', 'name')

    def get_current(self, id):
        return self.prefetch_related('company').get(id=id)


class Company(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'company'
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Icecreams(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    image = models.ImageField('картинка', upload_to='icecreams/')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='компания',
                                related_name='icecream_company')
    price = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)

    objects = IcecreamManager()

    class Meta:
        managed = False
        db_table = 'icecreams'
        verbose_name = 'Мороженное'
        verbose_name_plural = 'Мороженное'
