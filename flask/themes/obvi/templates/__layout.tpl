<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8" />
		<title>{% block title %}{% endblock %}</title>
		<link rel="stylesheet" type="text/css" href="/static/css/main.css" />
		<!--<script src="script.js"></script>-->
	</head>
	<body>
		<div id="outer">
			{% include "_nav.tpl" %}
			{% block body_content %}{% endblock %}
			<div class="clear"></div>
		</div>
	</body>
</html>