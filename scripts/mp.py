import multiprocessing
import time

def sleep(x):
    print(f'Sleeping for {x} seconds....')
    time.sleep(x)
    print(f'Done sleeping for {x} seconds!')

def main():
    start = time.perf_counter()

    p1 = multiprocessing.Process(target=sleep, args=[1.5])
    p2 = multiprocessing.Process(target=sleep, args=[1.5])

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish = time.perf_counter()
    print(finish - start)

if __name__ == '__main__':
    main()

