{# Start a new thread. #}
<form action="/thread/create" method="post">
	{{ thread_create_form.hidden_tag() }}
	{{ thread_create_form.new_thread_title.label }}<br />
	{{ thread_create_form.new_thread_title(placeholder='Subject of new thread') }}<br />
	{{ thread_create_form.post_content.label }}<br />
	{{ thread_create_form.post_content(placeholder='The content of your post') }}<br />
	<button class="post_submit" type="submit">Start New Thread</button>
</form>

