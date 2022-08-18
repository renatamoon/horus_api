# PROJECT IMPORTS
from src.router.router import app

# THIRD PART IMPORTS
from asgiref.wsgi import WsgiToAsgi


asgi_app = WsgiToAsgi(app)
