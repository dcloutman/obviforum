{% extends "__layout.tpl" %}
{% block title %}Create an Account{% endblock %}
{% block body_content %}
	<h1>Sign Up</h1>
	{% include '_flash.tpl' %}

	{% if not user_is_authenticated %}
	<h2>Create an Account</h2>
	<form action="/user/create" method="post">
		{{ signup_form.hidden_tag() }}
		<table cellpadding="0" cellspacing="0" border="0" class="form-table">
			<tr>
				<td>{{ signup_form.email.label }}</td>
				<td>{{ signup_form.email }}</td>
				<td class="field-description">Please use your real email address.</td>
			</tr>
			<tr>
				<td>{{ signup_form.username.label }}</td>
				<td>{{ signup_form.username }}</td>
				<td class="field-description">All letters will be converted to lower case.</td>
			</tr>
			<tr>
				<td>{{ signup_form.password.label }}</td>
				<td>{{ signup_form.password }}</td>
				<td class="field-description">Your password must be at least 8 characters long.</td>
			</tr>
			<tr>
				<td>{{ signup_form.password_confirm.label }}</td>
				<td>{{ signup_form.password_confirm }}</td>
				<td class="field-description">This must match your password exactly.</td>
			</tr>
			<tr>
				<td colspan="3" style="text-align: center;">
					<button class="post_submit" type="submit">Create Account</button>
				</td>
			</tr>
		</table>
	</form>
	{% endif %}
{% endblock %}
