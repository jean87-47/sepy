from django.test import TestCase

# Create your tests here.
<form action="{% url 'articles:comments' pk=article.pk %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">

</form>

<h3><a href="{% url 'accounts:signup' %}">계정 만들기</a></h3>