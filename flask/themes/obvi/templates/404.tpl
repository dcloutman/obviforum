{% extends "__layout.tpl" %}
{% block title %}404 Page Not Found{% endblock %}
{% block body_content %}
	<article>
		<header>
			<h1>404 Page Not Found</h1>
		</header>
	{% include '_flash.tpl' %}
	<p>
		The page you are seeking could not be found. Sorry!
	</p>
	</article>
{% endblock %}
