import csv
import glob
from multiprocessing import Process

class FileSearcher():
    def __call__(self,name,lfn,path_to_write):
        
        def csv_reader(name,lfn):
            '''
            Поиск числа в файле
            Вернет кол-во вхождений
            '''
            with open(name,'r') as current_csv:
                #reader = csv.reader(current_csv)
                global_count = 0
                for row in current_csv:
                    #row = map(int(),row)
                    global_count += row.count(str(lfn))
            return global_count

        def csv_writer(name,lfn,global_count):
            data = {'file_name': name,'looking_for_number':lfn,'count':global_count}
            with open(path_to_write,'a') as local_csv:
                writer = csv.writer(local_csv,delimiter=',')
                #for row in data:
                writer.writerow(data)

        #def main(name,lfn,path_to_write):
        global_count = csv_reader(name,lfn)
        csv_writer(name,lfn,global_count)

if __name__ == '__main__':
    
    lfn = 10
    n_processes = 10
    c_processes = 0
    files = glob.glob("D:\\sber\\Problem2\\*.csv")
    path_to_write = "D:\\sber\\Problem2\\stats.csv" # + filename
    procs = []
    while True:
        try:
            if len(files) != 0 and c_processes < n_processes:  
                name = files.pop()
                c_processes += 1
                t = FileSearcher()
                proc = Process(target = t,kwargs={'name':name,'lfn':lfn,'path_to_write':path_to_write})
                procs.append(proc)
                proc.start()
                #if len(files) != 0:
                #    continue
            elif len(files) == 0:
                c_processes -= 1
                proc.join()
            elif c_processes == n_processes:
                proc.join()
        except:
            if len(files) == 0: # если вдруг перед потоком, другой поток украл последний файл
                for proc in procs:
                    proc.join()
            elif c_processes == n_processes:
                continue
            else:
                continue
