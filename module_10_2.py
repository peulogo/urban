from threading import Thread
from time import sleep

class Knight(Thread):
    enemies = 100

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        days = 0
        print(f"{self.name}, на нас напали!")
        
        while Knight.enemies > 0:
            days += 1
            sleep(1)
            Knight.enemies -= self.power
            
            if Knight.enemies > 0:
                print(f"{self.name} сражается {days} день(дня)..., осталось {Knight.enemies} воинов.")
            else:
                Knight.enemies = 0
                print(f"{self.name} одержал победу спустя {days} день(дня)!")
                break

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")
