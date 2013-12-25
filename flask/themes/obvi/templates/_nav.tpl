<nav>
	<a href="/">Home</a>
	{% if user_is_authorized %}
	<a href="/login">Login</a>
	{% else %}
	<a href="/logout">Logout</a>
	{% endif %}
</nav>
