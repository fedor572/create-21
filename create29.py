import time
class Thread:
    pass


class Knight(Thread):
    def __init__(self, name, power, enemies):
        self.name = str(name)
        self.power = int(power)
        self.enemies = 100


    def run(self):
        print(f"{self.name}, на нас напали!")
        days = 0
        while self.enemies > 0:
            self.enemies -= self.power
            days += 1
            print(f"{self.name} сражается {days} , осталось {self.enemies} воинов")
            time.sleep(1)
        if self.enemies == 0:
            print(f"{self.name} одержал победу спустя {days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
