from app import app
application = app
if __name__ == "__main__":
    application.run(host="localhost", port=8090,debug=True,threaded=True)