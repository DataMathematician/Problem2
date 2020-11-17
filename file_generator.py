import os
import random
from multiprocessing import Process

class FileGen():
    def __call__(self,n_files,path,file_num,len_str,size):

        def string_generator(len_str):
            '''
            Генератор строки
            '''
            nums = []                                       
            for i in range(len_str):                       
                nums.append(str(random.randrange(0,100)))         
            yield nums

        def filemaker(n_name, p):
            '''
            Генератор
            '''
            name = 'num_data_{}.csv'.format(n_name)
            name = path+name
            new_file = open(name,'w')
            while os.stat(name).st_size < size:
                string = ','.join(list(string_generator(len_str))[0]) 
                #string = ','.join((list((str(random.randrange(0,100)) for x in range(len_str))))) # генератор строки, которая кладется в файл
                new_file.write(string)

        for i in range(n_files):
            filemaker(file_num, path)

path = 'D:\\sber\\Problem2\\'  # расположение файла
n_files = 2
len_str = 1000
size = 1073741824

if __name__ == '__main__':

    path = 'D:\\sber\\Problem2\\'  # расположение файла
    len_str = 100000
    size = 1073741824
    n_files = 20

    procs = []
    for num in range(n_files):
        t = FileGen()
        proc = Process(target = t,kwargs={'n_files':1,'path':'D:\\sber\\Problem2\\','file_num': num,'len_str':len_str,'size':1073741824})
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()