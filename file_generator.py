import multiprocessing as mp
import time
from numpy import random
from timeit import default_timer as timer
import sys

def worker(chunk_size,n_process, q):
    '''stupidly simulates long running process'''

    start = time.clock()
    nums = []
    print(q)
    while sys.getsizeof(nums) <= chunk_size:
        e =random.randint(100,size = 500)
        e = map(str,e)
        e = ','.join(e)+'\n'
        nums.append(e)
  
    done = time.clock() - start
    print('Done:', str(sys.getsizeof(nums)), done)
    q.put(nums)
    return nums

def listener(name,q):
    '''listens for messages on the q, writes to file. '''

    with open(name, 'w') as f:
        while 1:
            m = q.get()
            print(sys.getsizeof(m))
            if m == 'kill':
                break
            f.writelines(m)
            f.flush()

def main(name):
    #must use Manager queue here, or will not work
    manager = mp.Manager()
    q = manager.Queue()    
    pool = mp.Pool(mp.cpu_count())

    #put listener to work first
    watcher = pool.apply_async(listener, (name, q))

    #fire off workers
    jobs = []
    for i in range(n_process):
        job = pool.apply_async(worker, (chunk_size,n_process, q))
        jobs.append(job)

    # collect results from the workers through the pool result queue
    for job in jobs: 
        job.get()

    #now we are done, kill the listener
    q.put('kill')
    pool.close()
    pool.join()

if __name__ == "__main__":
    size = 6850000  # размер файла
    n_files = 20    # кол-во файлов
    n_process = 16 # кол-во процессов
    chunk_size = size / n_process 
    path = 'D:\\sber\\Problem2\\'

    for f in range(n_files):
        print('File: ',f)
        name = path + 'test_data_{}.txt'.format(f)
        main(name)
        print()
        print()