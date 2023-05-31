from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class Department(models.Model):
    title = models.CharField(max_length=255)
    admin = models.OneToOneField('Employee', on_delete=models.SET_NULL, null=True, blank=True, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class Employee(models.Model):
    first_name = models.CharField("first name", max_length=150, blank=True)
    last_name = models.CharField("last name", max_length=150, blank=True, db_index=True)
    father_name = models.CharField("Father name", max_length=150, blank=True)
    photo = models.ImageField(upload_to='fake_path', null=True, blank=True)
    pay = models.DecimalField(max_digits=9, decimal_places=2)
    old = models.PositiveSmallIntegerField()
    current_department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.father_name}'

    def __repr__(self):
        return f'{self.last_name} {self.first_name} {self.father_name}'

