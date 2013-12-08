{% extends "__layout.tpl" %}
{% block title %}Welcome to Bloggle{% endblock %}
{% block body_content %}
	<a href="/">Home</a>

	<h1>Thread #{{ thread_id }} Topic</h1>
	<ul>
		<li>
			<strong>Username 1</strong>
			<div>
				<p>
					Helvetica distillery gluten-free, before they sold out typewriter forage Cosby sweater. Drinking vinegar organic 90's raw denim. Locavore distillery scenester, Banksy stumptown flexitarian narwhal forage Wes Anderson literally wayfarers hashtag cray biodiesel. Fingerstache artisan mustache, viral stumptown swag ennui skateboard Echo Park ethnic Thundercats. Beard food truck selvage, 90's mumblecore bitters gluten-free messenger bag swag bespoke. Biodiesel gluten-free fanny pack irony. Mumblecore seitan four loko Vice deep v.
				</p>
			</div>
		</li>
		<li>
			<strong>Username 2</strong>
			<div>
				<p>
					Fugiat narwhal labore meh minim tote bag enim, vegan wayfarers sint velit esse typewriter exercitation. Jean shorts mustache fixie sapiente Williamsburg authentic. Duis synth church-key American Apparel jean shorts fingerstache. McSweeney's jean shorts duis cred Neutra squid sriracha. Hoodie tofu Marfa, odio chambray pariatur ex banh mi street art nesciunt post-ironic culpa veniam ut labore. Synth actually dolor, est slow-carb 8-bit Banksy yr flannel four loko. Viral twee beard, banjo assumenda 90's flexitarian vegan meggings blog trust fund keytar velit fingerstache.
				</p>
				<p>
					Shabby chic dolore American Apparel master cleanse nulla. Pug lo-fi craft beer sunt elit, food truck tousled yr. Austin you probably haven't heard of them sed, mixtape flannel hashtag pour-over cred. Fashion axe Blue Bottle food truck, tofu dolor sustainable non chia ea. Authentic cillum viral proident, farm-to-table ethnic cray PBR&amp;B minim. Austin culpa adipisicing, letterpress nulla shabby chic placeat forage church-key. Neutra excepteur try-hard YOLO, keffiyeh Intelligentsia nulla.
				</p>
			</div>
		</li>
		<li>
			<strong>Username 1</strong>
			<div>
				<p>
					Meggings banjo roof party bespoke. Typewriter sriracha asymmetrical irony. Bitters vinyl fap DIY stumptown pug, sustainable dreamcatcher bicycle rights aesthetic forage iPhone sartorial distillery. 90's sustainable 3 wolf moon gastropub hashtag Marfa. Squid hoodie fingerstache viral Williamsburg Portland. Vegan XOXO YOLO cliche Tonx, letterpress twee messenger bag gentrify. Direct trade fingerstache wayfarers cornhole typewriter gastropub, you probably haven't heard of them mustache XOXO scenester leggings wolf aesthetic.
				</p>
			</div>
		</li>
		<li>
			<strong>Username 3</strong>
			<div>
				<p>
					Me too.
				</p>
			</div>
		</li>
	</ul>

	<h2>Post Response</h2>
	<form action="/thread/create" method="post">
		<label for="thread_response">Message</label>
		<textarea class="post_content" id="thread_response"></textarea>
		<button class="post_submit" type="submit">Post Response</button>
	</form>

{% endblock %}