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
	<form action="/thread/create" method="post">
		{{ thread_create_form.hidden_tag() }}
		{{ thread_create_form.new_thread_title.label }}<br />
		{{ thread_create_form.new_thread_title(placeholder='Subject of new thread') }}<br />
		{{ thread_create_form.post_content.label }}<br />
		{{ thread_create_form.post_content(placeholder='The content of your post') }}<br />
		<button class="post_submit" type="submit">Start New Thread</button>
	</form>
	{% else %}
		{% include '_login.tpl' %}
	{% endif %}

	<h2>Current Discussions</h2>
	<ul>
	{% for thread in threads %}	
		<li><a href="/thread/{{ thread.thread_id }}">{{ thread.subject }}</a> <strong>Started by</strong> {{ thread.originator.username }} <strong>on</strong> <time>{{ thread.time_started }}</time></li>
	{% endfor %}
	</ul>

{% endblock %}
