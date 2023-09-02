import time
import asyncio
from threading import Thread

# Многопоточность
def red():
    time.sleep(5)
    return 'Красный'

def yellow(color_1: str):
    time.sleep(3)
    print('Желтый')


def green():
    time.sleep(8)
    return 'Зеленый'


t1 = Thread(target=yellow, args=['Зеленый'])
t1.start()
print(red())
print(green())
print('Старт!!!')




