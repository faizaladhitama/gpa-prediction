<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<script src="/static/js/utils.js"></script> 
<title>SSO UI</title>
</head>
<body>
        <div class="login-box">
                {% for message in messages %}
                <div class="alert {{ message.tags }} alert-dismissible" role="alert" id="django-messages">
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close" style="margin-right: 15px;">
                        <span aria-hidden="true">&times;</span>
                    </button>
                    {{ message }}
                </div>
                {% endfor %}

                <div class="top">
                        <h1>SSO</h1>
                        <div class="sub">Single Sign On - DEV</div>
                </div>
                <form action="{% url 'api:auth-login' %}" method="POST">                
                        {% csrf_token %}
                        <div class="middle">
                                <p>Masukkan username dan password UI Anda/<br /><em>Enter your username and password</em>:</p>
                                <div class="form-group">                
                                        <input id="username" name="username" class="form-control" placeholder="Username" type="text" value="" autocomplete="false"/>
                                                                        
                                </div>
                                <div class="form-group">
                                        <input id="password" name="password" class="form-control" placeholder="Password" type="password" value="" autocomplete="off"/>
                                </div>
                        </div>
                        <div class="bottom clearfix">
                                <div class="pull-right" style="margin-top:12px">
                                        <input type="submit" class="btn btn-lg btn-primary" value="Login"></input>
                                </div>
                        </div>
                </form>
        </div>
</body>
</html>


