from requests import get
from time import sleep
from threading import Thread


class Abuse:
    def __init__(self):
        self.thr = Thread(target=self.wait_mode)
        self.thr.start()

    def wait_mode(self):
        sleep(1500)  # 25 minutes
        get('https://gasnake.herokuapp.com/')
        self.wait_mode()
