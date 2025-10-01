import random
import time
import multiprocessing as mp
timeCount = 3

def printTime(timeout) :
    print('printing time...')
    time.sleep(timeout)
    print(time.ctime(time.time()))

if __name__ == '__main__':
    processes = []
    for i in range(timeCount):
        timeout = random.random()
        p = mp.Process(target=printTime, args=(timeout,))
        processes.append(p)
        p.start()
        for p in processes:
            p.join()

        