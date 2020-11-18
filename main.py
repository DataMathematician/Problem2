import csv
import glob
#import pandas as pd

class Result():
        
    def findNumber(self,files,lfn):

        def csv_reader(name,lfn):
            '''
            Поиск числа в файле
            Вернет кол-во вхождений
            '''
            with open(name,'r') as current_csv:
                global_count = 0
                for row in current_csv:
                    t = len(row)
                    global_count += row.count(str(lfn))
            return global_count

        #def csv_writer(name,lfn,global_count):
        #    pass
        #    #fieldnames = ['file_name','looking_for_number','count']
        #    #data = {'file_name': name,'looking_for_number':lfn,'count':global_count}
        #    #df = pd.DataFrame(data = data,index =[0])
        #    #with open(path_to_write, 'a') as f:
        #    #    df.to_csv(f, header=f.tell()==0,index =False)
        #
        #csv_writer(name,lfn,global_count)
            
        global_count = csv_reader(name,lfn)


if __name__ == '__main__':
    
while True:
    try:
        while True:
            #lfn = int(input('Введите число для поиска: '))
            #files = input('Введите деректорию для поиска [D:\\data\\]: ' ) #D:\sber\Problem2\
            lfn = 14
            files = 'D:\\sber\\Problem2\\'
            files = glob.glob(files + "*.csv")
            while len(files) != 0:
                name = files.pop()
                t = Result()            #   __call__
                t.findNumber(name,lfn)  # t.__call__
    except:
        continue
    
