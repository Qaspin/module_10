from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали')
        warriors = 100
        days = 0
        while warriors > 0:
            sleep(1)
            days += 1
            warriors -= self.power
            print(f'{self.name} сражается {days} суток, осталось {warriors} воинов врага.')
        print(f'{self.name} одержал победу спустя {days} дней(я)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Сражения закончены!")

