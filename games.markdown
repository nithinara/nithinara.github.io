---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

{% for game in site.games %}
<a href="{{ game.url }}">{{ game.title }}</a>
{% endfor %}