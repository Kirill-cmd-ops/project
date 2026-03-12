from flask import Flask
from routers.submission import submission_router
from routers.views import views_router

app = Flask(__name__)
app.register_blueprint(submission_router)
app.register_blueprint(views_router)
