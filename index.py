from multiprocessing import Process
from model import snake_processing
from os import environ


class Model:

    def __init__(self):
        self.proc = Process(target=snake_processing.PlaySnake().execute)

    def run_process(self):
        print('Start model training')
        self.proc.start()

    def stop_process(self):
        self.proc.join()
