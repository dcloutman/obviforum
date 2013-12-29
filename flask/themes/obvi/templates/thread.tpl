{% extends "__layout.tpl" %}
{% block title %}{{ thread_subject }}{% endblock %}
{% block body_content %}
	<article>
		<header>
			<h1>{{ thread.subject }}</h1>
		</header>
	{% include '_flash.tpl' %}

	{% for post in posts %}
		<article>
			<header>
				<strong>{{ post.user.username }}</strong> <time datetime="2013-12-02">{{ post.post_datetime }}</time>
			</header>
			<p>
				{{ post.post_message }}
			</p>
		</article>
	{% endfor %}
	</article>

	{% if user_is_authenticated %}
	<h2>Post a Response</h2>
	<form action="/thread/respond" method="post">
		<input type="hidden" name="thread_id" value="{{ thread.thread_id }}" /> 
		<label for="thread_response">Message</label><br />
		<textarea class="post_content" id="thread_response" name="post_content"></textarea><br />
		<button class="post_submit" type="submit">Post Response</button>
	</form>
	{% else %}
		<h2>Login to Join the Conversation</h2>
		{% include '_login.tpl' %}
	{% endif %}
{% endblock %}