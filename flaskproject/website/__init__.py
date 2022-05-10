from flask import Flask


def creat_app():
    app = Flask(__name__)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, prefix_url="/")
    app.register_blueprint(auth, prefix_url="/")

    return app
