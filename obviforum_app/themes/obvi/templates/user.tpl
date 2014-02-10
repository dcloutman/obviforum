{% extends "__layout.tpl" %}
{% block title %}Your Profile{% endblock %}
{% block body_content %}
	<article>
		<header>
			<h1>Profile for {{ authenticated_user.username }}</h1>
		</header>

		<section>
			<header>
				<h2>Statistics</h2>
			</header>
			<dl>
				<dt>Number of Posts:</dt>
				<dd>{{ num_posts }}</dd>
				<dt>Most Recent Post Date:</dt>
				<dt>{{ most_recent_post_date }}</dt>
				<dt>First Post Date:</dt>
				<dd>{{ first_post_date }}</dd>
			</dl>
		</section>

		<section>
			<header>
				<h2>Threads You Started</h2>
			</header>
			<ul>
	{% for thread in threads %}	
				<li><a href="/thread/{{ thread.thread_id }}">{{ thread.subject }}</a> <time>{{ thread.time_started }}</time></li>
	{% endfor %}
			</ul>
		</section>
	</article>

{% endblock %}
