# PROJECT IMPORTS
import uvicorn
from src.routers.routers import app

# THIRD PART IMPORTS
from asgiref.wsgi import WsgiToAsgi

asgi_app = WsgiToAsgi(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
