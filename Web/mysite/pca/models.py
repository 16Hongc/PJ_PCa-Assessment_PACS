from django.db import models

# Create your models here.


class patient_info(models.Model):
    # patient_info라는 모델안에 models.Model을 상속받는다는 뜻.
    # 모델클래스는 반드시 models.Model을 상속받아야 함.
    patient_id = models.AutoField()
    name = models.CharField(max_length=10)
    birth_date = models.TextField()
    address = models.TextField()
    visit_date = models.DateTimeField()   # 날짜만 가질 경우는 DateField / 시간만 가질 경우는 TimeField
    phone_number = models.IntegerField(default=0)


