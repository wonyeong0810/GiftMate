from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from main.models import Recommendation

# Create your views here.
def index(request):
    if request.method == 'POST':
        return recommendationCreate(request)
    return render(request, 'index.html')

def recommendationCreate(request):
    recommendation = Recommendation.objects.create(
            relationship=request.POST.get('relationship'),
            closeness=int(request.POST.get('closeness')),
            duration=int(request.POST.get('duration')),
            region=request.POST.get('region'),
            attendance=request.POST.get('attendance'),
            budget_min=request.POST.get('budget_min') or None,
            budget_max=request.POST.get('budget_max') or None,
            additional_info=request.POST.get('additionalInfo', '')
        )
    return render(request, 'result.html', {'recommendation': recommendation})

# 돈 계산 AI
import openai

def recommend_cash_gift_with_gpt(
    relationship,
    closeness,
    duration,
    region,
    attendance,
    budget_min=None,
    budget_max=None,
    api_key=None
):
    prompt = f"""
다음 조건을 바탕으로 축의금 금액을 추천해줘. 금액은 한국 원화로 제시하고, 추천 사유 없이 금액만 숫자로 알려줘.

- 관계: {relationship}
- 친밀도: {closeness} (1~5, 숫자가 높을수록 더 친함)
- 알고 지낸 기간: {duration}년
- 지역: {region}
- 참석 여부: {attendance}
"""

    if budget_min:
        prompt += f"- 최소 예산: {budget_min}원\n"
    if budget_max:
        prompt += f"- 최대 예산: {budget_max}원\n"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        api_key=api_key,
        messages=[
            {"role": "system", "content": "너는 축의금 추천 전문가야. 결과는 금액 숫자만 보여줘."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=10
    )

    # 숫자만 추출
    answer = response['choices'][0]['message']['content']
    return int(''.join(filter(str.isdigit, answer)))