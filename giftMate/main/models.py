from django.db import models

# Create your models here.
class Recommendation(models.Model):
    RELATIONSHIP_CHOICES = [
        ('family', '가족'),
        ('friend', '친구'),
        ('coworker', '직장동료'),
        ('relative', '친척'),
    ]

    REGION_CHOICES = [
        ('seoul', '서울'),
        ('gyeonggi', '경기'),
        ('incheon', '인천'),
        ('busan', '부산'),
        ('daegu', '대구'),
        ('daejeon', '대전'),
        ('ulsan', '울산'),
        ('gangwon', '강원'),
        ('chungbuk', '충북'),
        ('chungnam', '충남'),
        ('jeonbuk', '전북'),
        ('jeonnam', '전남'),
        ('gyeongbuk', '경북'),
        ('gyeongnam', '경남'),
        ('jeju', '제주'),
    ]

    ATTENDANCE_CHOICES = [
        ('yes', '참석'),
        ('no', '불참'),
    ]

    relationship = models.CharField(max_length=20, choices=RELATIONSHIP_CHOICES)
    closeness = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    duration = models.IntegerField(help_text="알고 지낸 기간 (년 단위)")
    region = models.CharField(max_length=20, choices=REGION_CHOICES)
    attendance = models.CharField(max_length=3, choices=ATTENDANCE_CHOICES)
    budget_min = models.PositiveIntegerField(null=True, blank=True)
    budget_max = models.PositiveIntegerField(null=True, blank=True)
    additional_info = models.TextField(blank=True)
    answer = models.IntegerField(null=True, blank=True, help_text="추천된 답변 가격")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_relationship_display()} - {self.region} - {self.attendance}"