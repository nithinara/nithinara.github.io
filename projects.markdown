---
layout: page
title: Projects
---

{% assign col = page.title | downcase %}
{% for item in site[col] %}
<a href="{{ item.url }}">{{ item.title }}</a>
{% endfor %}