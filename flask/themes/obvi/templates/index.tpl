{% extends "__layout.tpl" %}
{% block title %}Welcome to ObviForums{% endblock %}
{% block body_content %}
	<h1>Welcome {{ first_username }}</h1>
	<p>
		Fashion axe Blue Bottle food truck, tofu dolor sustainable non chia ea. Authentic cillum viral proident, farm-to-table ethnic cray PBR&amp;B minim.
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
	{%endif %}

	<h2>Current Discussions</h2>
	<ul>
		<li><a href="/thread/1">Thread 1</a></li>
		<li><a href="/thread/2">Thread 2</a></li>
		<li><a href="/thread/3">Thread 3</a></li>
		<li><a href="/thread/4">Thread 4</a></li>
		<li><a href="/thread/5">Thread 5</a></li>
		<li><a href="/thread/6">Thread 6</a></li>
		<li><a href="/thread/7">Thread 7</a></li>
		<li><a href="/thread/8">Thread 8</a></li>
		<li><a href="/thread/9">Thread 9</a></li>
		<li><a href="/thread/10">Thread 10</a></li>
	</ul>

{% endblock %}