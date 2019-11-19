from multiprocessing import Process
from model import snake_processing
from os import environ
import time

PORT_NUMBER = int(environ["PORT"])


class Model:
    def __init__(self):
        self.proc = Process(target=snake_processing.PlaySnake().execute)

    def run_process(self):
        print("Start model")
        self.proc.start()

    def stop_process(self):
        self.proc.join()


try:
    model = Model()
    print(f'Start model on process: {PORT_NUMBER}')
    model.run_process()
except KeyboardInterrupt:
    print('^C received, shutting down training')
    model.stop_process()
