from routes import APP
import settings

def run_server():
    APP.run(host=settings.HOST_NAME,port=settings.HOST_PORT,debug=settings.HOST_DEBUG)

