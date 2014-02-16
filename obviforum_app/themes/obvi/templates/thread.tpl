{% extends "__layout.tpl" %}
{% block title %}{{ thread_subject }}{% endblock %}
{% block body_content %}
	<article>
		<header>
			<h1>{{ thread.subject }}</h1>
		</header>
	{% include '_flash.tpl' %}

	{% for post in posts %}
		<article class="thread-container">
			<header>
				<strong>{{ post.user.username }}</strong> <time datetime="2013-12-02">{{ post.post_datetime | display_date }}</time>
			</header>
			<div class="post-body">
				{{ post.post_message | nl2br }}
			</div>
		</article>
	{% endfor %}
	</article>

	{% if user_is_authenticated %}
	<h2>Post a Response</h2>
	<form action="/thread/respond" method="post">
		{{ response_form.hidden_tag() }}
		{{ response_form.thread_id }} 
		{{ response_form.post_content.label }}<br />
		{{ response_form.post_content }}<br />
		<button class="post_submit" type="submit">Post Response</button>
	</form>
	{% else %}
		<h2>Login to Join the Conversation</h2>
		{% include '_login.tpl' %}
	{% endif %}
{% endblock %}
