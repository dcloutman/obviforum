<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8" />
		<title>{% block title %}{% endblock %}</title>
		{% include '_custom_head_tags.tpl' %}
	</head>
	<body>
		{% include '_javascript_before_opening_body.tpl' %}
		<main>
			{% include "_nav.tpl" %}
			<div id="body_content_container">
				{% block body_content %}{% endblock %}
				<div class="clear"></div>
			</div>
			{% include "_footer.tpl" %}
			<div class="clear"></div>
		</main>
		{% include '_javascript_before_closing_body.tpl' %}
	</body>
</html>
