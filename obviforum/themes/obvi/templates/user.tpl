{% extends "__layout.tpl" %}
{% block title %}Your Profile{% endblock %}
{% block body_content %}
	<article>
		<header>
			<h1>Profile for {{ authenticated_user.username }}</h1>
		</header>
	{% include '_flash.tpl' %}

		<section>
			<header>
				<h2>Statistics</h2>
			</header>

			<strong>Number of Posts:</strong> {{ num_posts }}<br />
			<strong>Most Recent Post Date:</strong> {{ most_recent_post_date | display_date }}<br />
			<strong>First Post Date:</strong> {{ first_post_date | display_date }}<br />
		</section>

		<section>
			<header>
				<h2>Threads You Started</h2>
			</header>
	{% if threads %}
			<ul>
		{% for thread in threads %}	
				<li><a href="/thread/{{ thread.thread_id }}">{{ thread.subject }}</a> <time>{{ thread.time_started | display_date }}</time></li>
		{% endfor %}
			</ul>
	{% else %}
		<em>You have not started any threads.</em> Start one now:
		{% include '_new_thread_form.tpl' %}		
	{% endif %}
		</section>
	</article>

{% endblock %}
