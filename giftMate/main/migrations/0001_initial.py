# Generated by Django 5.2.1 on 2025-06-04 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Recommendation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "relationship",
                    models.CharField(
                        choices=[
                            ("family", "가족"),
                            ("friend", "친구"),
                            ("coworker", "직장동료"),
                            ("relative", "친척"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "closeness",
                    models.IntegerField(
                        choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")]
                    ),
                ),
                ("duration", models.IntegerField(help_text="알고 지낸 기간 (년 단위)")),
                (
                    "region",
                    models.CharField(
                        choices=[
                            ("seoul", "서울"),
                            ("gyeonggi", "경기"),
                            ("incheon", "인천"),
                            ("busan", "부산"),
                            ("daegu", "대구"),
                            ("daejeon", "대전"),
                            ("ulsan", "울산"),
                            ("gangwon", "강원"),
                            ("chungbuk", "충북"),
                            ("chungnam", "충남"),
                            ("jeonbuk", "전북"),
                            ("jeonnam", "전남"),
                            ("gyeongbuk", "경북"),
                            ("gyeongnam", "경남"),
                            ("jeju", "제주"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "attendance",
                    models.CharField(
                        choices=[("yes", "참석"), ("no", "불참")], max_length=3
                    ),
                ),
                ("budget_min", models.PositiveIntegerField(blank=True, null=True)),
                ("budget_max", models.PositiveIntegerField(blank=True, null=True)),
                ("additional_info", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
