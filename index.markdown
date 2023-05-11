---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

Hello! Check out my thoughts on these various subjects:

{% for collection in site.collections %}
{% if collection.label != 'posts' %}
<a href="{{ collection.label }}">{{ collection.label | capitalize }}</a>
{% endif %}
{% endfor %}