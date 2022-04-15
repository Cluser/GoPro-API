import threading
from api import general as api

class Main():

    def __init__(self) -> None:
        pass

    def api_thread():
        apiOb = api.Api()
        apiOb.run()
        pass

    if __name__ == "__main__":
        apiThread = threading.Thread(target = api_thread)
        apiThread.start()
