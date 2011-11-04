<html>
    <head>
        <meta http-equiv="Content-type" content="text/html; charset=utf-8"/>
        <title>{% block title %}{{ title }}{% endblock %} - YouTube Linker</title>
        <script type="text/javascript" charset="utf-8" src="http://code.jquery.com/jquery-1.7.min.js"></script>
        <link rel="stylesheet" href="/static/css/main.css" type="text/css" media="screen" charset="utf-8">
        {% block header %}
          
        {% endblock %}
    </head>
    
    <body>
        <div id="content">
        {% block content %}
            Content here
        {% endblock %}
        </div>
        <script type="text/javascript" charset="utf-8" src="/static/js/default.js"></script>
    </body>
</html>