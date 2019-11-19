from multiprocessing import Process
from model import snake_processing
from os import environ


class Model:

    def __init__(self):
        self.proc = Process(target=snake_processing.PlaySnake().execute)

    def run_process(self):
        PORT_NUMBER = int(environ["PORT"])
        print(f'Start model on process: {PORT_NUMBER}')
        self.proc.start()

    def stop_process(self):
        self.proc.join()
