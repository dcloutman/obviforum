{# A stand-alone login page. #}
{% extends "__layout.tpl" %}
{% block title %}Login{% endblock %}
{% block body_content %}
<h1>Login</h1>
{% include '_flash.tpl' %}
{% if user_is_authenticated %}
	{% include '_logout.tpl' %}
{% else %}
	{% include '_login.tpl' %}
{% endif %}
{% endblock %}