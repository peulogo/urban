from multiprocessing import Pool
import time

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    return all_data

def linear_read(filenames):
    all_data = []
    for filename in filenames:
        all_data.extend(read_info(filename))
    return all_data

def multiprocess_read(filenames):
    with Pool() as pool:
        results = pool.map(read_info, filenames)
    return results

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    linear_read(filenames)
    linear_time = time.time() - start_time
    print(f'\n {linear_time:.6f} (линейный)')

    # Многопроцессный вызов
    start_time = time.time()
    multiprocess_read(filenames)
    multiprocess_time = time.time() - start_time
    print(f'\n {multiprocess_time:.6f} (многопроцессный)')
