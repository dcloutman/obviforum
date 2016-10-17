{% extends "__layout.tpl" %}
{% block title %}Welcome to ObviForums{% endblock %}
{% block body_content %}
	<h1>Welcome {{ first_username }}</h1>
	<p>
		{{ welcome_text }}
	</p>
	{% include '_flash.tpl' %}

	{% if user_is_authenticated %}
	<h2>Start a New Discussion</h2>
		{% include '_new_thread_form.tpl' %}
	{% else %}
		{% include '_login.tpl' %}
	{% endif %}

	<h2>Current Discussions</h2>
	<ul>
	{% for thread in threads %}	
		<li><a href="/thread/{{ thread.thread_id }}">{{ thread.subject }}</a> <strong>Started by</strong> {{ thread.originator.username }} <strong>on</strong> <time>{{ thread.time_started | display_date }}</time></li>
	{% endfor %}
	</ul>

{% endblock %}
