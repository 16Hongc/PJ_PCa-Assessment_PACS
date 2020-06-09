from django.db import models
from django.conf import settings
from django.utils import timezone
from .models import *


# Create your models here.
class patient_info(models.Model) :
    # patient_info라는 모델안에 models.Model을 상속받는다는 뜻.
    # 모델클래스는 반드시 models.Model을 상속받아야 함.
    patient_id = models.AutoField(primary_key=True)    # 자동으로 번호를 채워줌
    name = models.CharField(max_length=10)
    birth_date = models.DateField()
    address = models.TextField()
    phone_number = models.IntegerField(default=0)

    # def __str__(self):   # string으로 리턴
    #     return self.patient_id, self.name, self.birth_date, self.address, self.phone_number


class treatment_list(models.Model) :
    patient_id = models.ForeignKey(patient_info, on_delete=models.CASCADE)   # patient_info의 키를 빌려옴
    visit_date = models.DateField(auto_now_add=True)  # 날짜만 가질 경우는 DateField / 시간만 가질 경우는 TimeField
    # biopsy_image =

    # def __str__(self):   # string으로 리턴
    #     return self.patient_id, self.visit_date
