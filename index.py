from multiprocessing import Process
from model import snake_processing
import time


class Model:
    def __init__(self):
        self.proc = Process(target=snake_processing.PlaySnake().execute)

    def run_process(self):
        print("Start model")
        self.proc.start()

    def stop_process(self):
        self.proc.join()


def common():
    print("I AM HERE")
#
# def data(request):
#     not_exist = True
#
#     while not_exist:
#         try:
#             open("home/Documents/sites/GASnake/data/coords.json")
#             not_exist = False
#         except FileNotFoundError:
#             time.sleep(1/4)
#
#     return render(request, 'home/Documents/sites/GASnake/data/coords.json')
#
#
# def blog(request):
#     return render(request, 'GASnake/index.html')


# model = Model()
# model.run_process()
