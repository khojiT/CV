from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from extensions.utill import convert_to_englishnum
from .manager import UserManager

def validate_mobile_number(value):
    value = convert_to_englishnum(value)
    if len(value) != 11 or not value.isdigit():
        raise ValidationError(
            _('%(value)s شماره موبایل معتبر نیست'),
            params={'value': value},
        )

def validate_melli_code(value):
    value = convert_to_englishnum(value)
    
    if len(value) != 10 or not value.isdigit():
        raise ValidationError(
            _('%(value)s کد ملی معتبر نیست.'),
            params={'value': value},
        )

# Create your models here.

USER_LEVEL = (
    ('1' , 'پایه'),
    ('2' , 'متوسط'),
    ('3' , 'پیشرفته'),
    ('4' , 'فوق پیشرفته'),
)

class User(AbstractUser):
    username = None

    mobile_number = models.CharField (max_length = 11, unique = True , validators = [validate_mobile_number] , verbose_name = 'شماره همراه')
    melli_code = models.CharField (max_length = 10 , unique=True ,validators = [validate_melli_code], null=True , blank= True , verbose_name = 'کد ملی')
    level = models.CharField(max_length = 1 ,default = '1',  choices = USER_LEVEL , verbose_name = 'سطح')
    birth_date = models.DateField(editable = True, blank = True , null = True , verbose_name = 'تاریخ تولد' )

    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = []

    objects = UserManager()
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
    
    def signupNo(self):
        first_of_day = self.date_joined.date()
        No = User.objects.filter(date_joined__gte = first_of_day , date_joined__lte = self.date_joined).count()
        return No
        
    def save(self, *args , **kwargs):
        self.melli_code = convert_to_englishnum(self.melli_code)
        self.mobile_number = convert_to_englishnum(self.mobile_number)
        super(User,self).save(*args,**kwargs)

    def __str__(self):
        return self.get_full_name()

