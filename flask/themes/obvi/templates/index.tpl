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
		<label for="new_thread_title">Thread Title</label><br />
		<input id="new_thread_title" class="post_title" type="text" placeholder="Subject of new thread" /><br />
		<label for="new_thread_content">Message</label><br />
		<textarea class="post_content" id="new_thread_content" placeholder="The content of your post"></textarea><br />
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
