from multiprocessing import Process
from requests import get
from time import sleep


class Abuse:

    def __init__(self):
        self.thr = Process(target=self.wait_mode)
        self.thr.start()

    def wait_mode(self):
        sleep(1500)  # 25 minutes
        get('https://gasnake.herokuapp.com/')
        self.wait_mode()

    def stop_thread(self):
        self.thr.terminate()
