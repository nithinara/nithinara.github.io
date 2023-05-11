---
layout: home
---

{% for item in site.food %}
<a href="{{ item.url }}">{{ item.title }}</a>
{% endfor %}