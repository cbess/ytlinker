<html>
    <head>
        <meta http-equiv="Content-type" content="text/html; charset=utf-8"/>
        <title>{% block title %}{{ title }}{% endblock %} - YouTube Linker</title>
        <link rel="stylesheet" href="/static/css/main.css" type="text/css" media="screen" charset="utf-8">
        {% block header %}
          
        {% endblock %}
    </head>
    <body id="">
        <div id="content">
        {% block content %}
            Content here
        {% endblock %}
        </div>
    </body>
</html>