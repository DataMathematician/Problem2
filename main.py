import csv
import glob
#from multiprocessing import Process
import pandas as pd

class FileSearcher():
    def __call__(self,name,lfn,path_to_write):
        
        def csv_reader(name,lfn):
            '''
            Поиск числа в файле
            Вернет кол-во вхождений
            '''
            with open(name,'r') as current_csv:
                global_count = 0
                for row in current_csv:
                    global_count += row.count(str(lfn))
            return global_count

        def csv_writer(name,lfn,global_count):
            fieldnames = ['file_name','looking_for_number','count']
            data = {'file_name': name,'looking_for_number':lfn,'count':global_count}
            df = pd.DataFrame(data = data,index =[0])
            with open(path_to_write, 'a') as f:
                df.to_csv(f, header=f.tell()==0,index =False)
            
                
        global_count = csv_reader(name,lfn)
        csv_writer(name,lfn,global_count)

if __name__ == '__main__':
    
    lfn = 10
    files = glob.glob("D:\\sber\\Problem2\\*.csv")
    path_to_write = "D:\\sber\\Problem2\\stats.csv" # + filename
    
    while len(files) != 0:
        name = files.pop()
        t = FileSearcher()
        t.__call__(name,lfn,path_to_write)
           
