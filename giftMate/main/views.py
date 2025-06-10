from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from main.models import Recommendation
from django.template.loader import get_template

# Create your views here.
def index(request):
    if request.method == 'POST':
        return recommendationCreate(request)
    return render(request, 'index.html')

def recommendationCreate(request):
    cash = recommend_cash_gift_with_gpt(request.POST.get('relationship'),
                                         int(request.POST.get('closeness')),
                                         int(request.POST.get('duration')),
                                         request.POST.get('region'),
                                         request.POST.get('attendance'),
                                         request.POST.get('budget_min') or None,
                                         request.POST.get('budget_max') or None,
                                         request.POST.get('additionalInfo', ''))
    
    recommendation = Recommendation.objects.create(
            relationship=request.POST.get('relationship'),
            closeness=int(request.POST.get('closeness')),
            duration=int(request.POST.get('duration')),
            region=request.POST.get('region'),
            attendance=request.POST.get('attendance'),
            budget_min=request.POST.get('budget_min') or None,
            budget_max=request.POST.get('budget_max') or None,
            additional_info=request.POST.get('additionalInfo', ''),
            answer = cash
        )
    
    return render(request, 'result.html', {'recommendation': recommendation, 'cash': cash}) 

# 돈 계산 AI
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()


client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

def recommend_cash_gift_with_gpt(
    relationship,
    closeness,
    duration,
    region,
    attendance,
    budget_min=None,
    budget_max=None,
    additional_info=None
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

    if additional_info != None and additional_info.strip():
        prompt += f"- 추가 정보: {additional_info}\n"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "너는 축의금 추천 전문가야. 결과는 금액 숫자만 보여줘. ex) 50000"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=30,
        temperature=0.4
    )
    
    answer = response.choices[0].message.content.strip()
    print(answer)
    return int(''.join(filter(str.isdigit, answer)))