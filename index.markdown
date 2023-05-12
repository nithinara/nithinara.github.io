---
layout: home
---

Hello! If you want to learn about my professional experience, check out my [about]({% link about.markdown %}) page!

You can also check out my musings on different topics:

{% for collection in site.collections %}
{% if collection.label != 'posts' %}
  <h2><a href="{{ collection.label }}">{{ collection.label | capitalize }}</a></h2>
{% endif %}
{% endfor %}