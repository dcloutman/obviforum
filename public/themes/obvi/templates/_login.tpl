{# A reusable login form. #}
<form method="POST" action="/login">
	{{ login_form.hidden_tag() }}
	{{ login_form.username.label }}
	{{ login_form.username }}
	{{ login_form.password.label }}
	{{ login_form.password }}
	<button type="submit">Login</button>
</form>
