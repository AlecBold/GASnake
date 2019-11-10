from django.shortcuts import render
from django.http import HttpResponse
from threading import Thread
from .train import snake_processing
import time


class MyThread(Thread):
    def __init__(self, go):
        Thread.__init__(self)
        self.request = None
        self.count = 0
        self.application_server = snake_processing.PlaySnake()

    def run(self):
        self.application_server.execute()


def data(request):
    not_exist = True

    while not_exist:
        try:
            open("GASnake/templates/GASnake/coordinates_snake.json")
            not_exist = False
        except FileNotFoundError:
            time.sleep(1/4)

    return render(request, 'GASnake/coordinates_snake.json')


def blog(request):
    return render(request, 'GASnake/index.html')


my_thread = MyThread(True)
my_thread.start()
