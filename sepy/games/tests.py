from django.test import TestCase

# Create your tests here.
<h2><a href="{% url 'accounts:signup' %}">계정만들기</a></h2>
<h2><a href="{% url 'accounts:login' %}">로그인</a></h2>
<h3><a href="{% url 'accounts:signup' %}">계정 만들기</a></h3>
<h3><a href="{% url 'accounts:detail' pk=request.user.pk %}">회원정보</a></h3>
<h3><a href="{% url 'accounts:logout' %}">로그아웃</a></h3>
<h3><a href="{% url 'accounts:login' %}">로그인</a></h3>