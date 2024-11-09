from time import sleep
import time
from threading import Thread

def write_words(word_count, file_name):
    with open(file_name, 'a') as file:
        for word_number in range(1, word_count+1):
            file.write(f'Какое-то слово № {word_number}\n')
            sleep(0.1)
    print(f'\n Завершилась запись в файл {file_name}.')

start_time = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
print(f"Время выполнения функций без потоков: {time.time() - start_time} секунд")

threads = [
    Thread(target=write_words, args=(10, 'example5.txt')),
    Thread(target=write_words, args=(30, 'example6.txt')),
    Thread(target=write_words, args=(200, 'example7.txt')),
    Thread(target=write_words, args=(100, 'example8.txt'))
]

start_time = time.time()
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(f"Время выполнения функций с потоками: {time.time() - start_time} секунд")
