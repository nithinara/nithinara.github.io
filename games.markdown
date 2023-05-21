---
layout: page
slug: Games
---

<h1>{{ page.slug }}</h1>

{% assign col = page.slug | downcase %}
{% for item in site[col] %}
<a href="{{ item.url }}">{{ item.title }}</a>
{% endfor %}