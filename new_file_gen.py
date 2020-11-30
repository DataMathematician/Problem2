import multiprocessing as mp
import sys
from numpy import random

from timeit import default_timer as timer
import time

class Worker:
    '''Генератор строк'''
    def work(n_process,chunk_size,q):
        start = time.clock()
        nums = []
        while sys.getsizeof(nums) <= chunk_size:
            e = random.randint(100,size = 500)
            e = map(str,e)
            e = ','.join(e)+'\n'
            nums.append(e)
        done = time.clock() - start
        print('Done: ',str(sys.getsizeof(nums)),done)
        q.put(nums)
        return nums

class Listener:
    '''Запись в файл'''
    def listen(n_process,name,q):
        print(name)
        with open(name, 'w') as f:
            strings_list = []
            while 1:
                m = q.get()
                strings_list.extend(m)
                print(sys.getsizeof(strings_list))
                if m == 'kill':
                    break
            f.writelines(strings_list)
            f.flush()

class Gen():
    '''Генератор файлов'''
    def __init__(self,name,chunk_size,n_process):
        self.name = name
        self.chunk_size = chunk_size
        self.n_process = n_process
    
    def generate(self):
        manager = mp.Manager()
        q = manager.Queue()
        pool = mp.Pool(mp.cpu_count())

        lis = Listener()
        watcher = pool.apply_async(lis.listen,(self.name,q))

        jobs = []
        for i in range(self.n_process):
            wor = Worker()
            job = pool.apply_async(wor.work,(self.chunk_size,q))
            jobs.append(job)

        for job in jobs:
            job.get()

        q.put('kill')
        pool.close()
        pool.join()

class TheCycle():
    '''Класс основного цикла'''
    def __init__(self,n_files = 20, size = 6850000, n_process = 16,path = 'D:\\sber\\Problem2\\'):
        self.n_files = n_files
        self.size = size
        self.n_process = n_process
        self.path = path
        self.chunk_size = self.size / self.n_process

    def start_cycle(self):
        for f in range(self.n_files):
            print('File: ',f)
            name = self.path + 'test_3_{}.txt'.format(f)

            file_obj = Gen(name,self.chunk_size,self.n_process)
            file_obj.generate()

if __name__ == "__main__":
    c = TheCycle()
    c.start_cycle()
    