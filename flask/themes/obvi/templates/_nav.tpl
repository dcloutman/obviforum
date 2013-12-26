<nav>
	<a href="/">Home</a>
	{% if user_is_authenticated %}
	Welcome {{ authenticated_user.username }}! <a href="/logout">Logout</a>
	{% else %}
	<a href="/login">Login</a>
	{% endif %}
</nav>
