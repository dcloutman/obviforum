<nav>
	<div class="navigation-column float-left text-align-left">
		<a href="/">Home</a>
	</div>

	<div class="navigation-column float-right text-align-right">
	{% if user_is_authenticated %}
		Welcome {{ authenticated_user.username }}! | <a href="/logout">Logout</a>
	{% else %}
		<a href="/signup">Sign Up</a> | <a href="/login">Login</a>
	{% endif %}
	</div>

	<div class="clear"></div>
</nav>
