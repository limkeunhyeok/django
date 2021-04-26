import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
# Question과 Choice는 django.db.models.Model.를 상속
# Charfield: 한 줄 정도의 문자
# DateTimeField: 날짜와 시간
# IntergerField: 숫자(정수)
# ForeignKey는 Choice와 Question을 연결해 주는 것으로 다대일(many-to-one) 관계로 설정(일대다, 다대다 관계로도 설정 가능)
# on_delete=models.CASCADE는 원래 데이터인 Question이 삭제될 경우 이 필드가 삭제된다는 의미

class Question(models.Model):
    quest_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # __str__은 객체의 표현에 사용
    def __str__(self):
        return self.quest_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # __str__은 객체의 표현에 사용
    def __str__(self):
        return self.choice_text
