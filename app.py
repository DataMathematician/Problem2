import glob
from flask import Flask,session

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def index():
    return "<h1>Enter value in searchstring after '/'</h1>"

@app.route('/<int:lfn>')
def findnumber(lfn):
    update_table()
    path = 'D:\\sber\\Problem2\\'
    files = glob.glob(path + "*.txt")
    while len(files) != 0:
        name = files.pop()
        with open(name,'r') as current_csv:
            global_count = 0
            for row in current_csv:
                global_count += row.count(str(lfn))
        update_records(name,global_count)
    zipped = zipping(session['names'],session['volumes'])
    return '<h1>%s</h1>' % zipped

def zipping(names,volumes):
    z = list(zip(names,volumes))
    return z

def update_table():
    session['names'] = []
    session['volumes'] = []

def update_records(name,volume):
    session['names'].append(name)
    session['volumes'].append(volume)

if __name__ == '__main__':
    app.run(debug=True)