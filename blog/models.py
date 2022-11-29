from django.db import models

# Create your models here.

class Facinfo(models.Model):
    fCode = models.IntegerField()             # 코드
    fName = models.CharField(max_length=50)   # 이름
    fModel = models.CharField(max_length=50)  # 모델
    fDesc = models.CharField(max_length=250)  # 설명

    def __str__(self):
        return self.fName 

class Essay(models.Model):
    fCode = models.IntegerField()             # 번호
    fTitle = models.CharField(max_length=50)  # 제목
    fTopic = models.CharField(max_length=50)  # 주제
    fWriter = models.CharField(max_length=50) # 글쓴이 
    fDesc = models.CharField(max_length=250)  # 설명

    def __str__(self):
        x = '[' + self.fTopic + '] ' + self.fTitle
        return x
    
class Music(models.Model):
    Music_Name = models.CharField(max_length=50)   # 노래 제목
    Music_Singer = models.CharField(max_length=50) # 노래 가수
    Music_Maker = models.CharField(max_length=50)  # 노래 작곡
    Music_Link = models.CharField(max_length=250)  # 노래 링크
    Music_Info = models.CharField(max_length=250)  # 노래 정보

    def __str__(self):
        x = self.Music_Singer + ' - ' + self.Music_Name
        return x
    
    