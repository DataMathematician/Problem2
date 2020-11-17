#from app import db, session, Base
import glob
import csv
import json

from flask import Flask,jsonify, request # request получение json от клиента серверу
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

#from  main import Result

app = Flask(__name__) # объект приложения

client = app.test_client()

engine = create_engine('sqlite:///db.sqlite')#!

session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))

Base = declarative_base() # базовый класс, содержит все, чтобы описать модель данных в пользоват.классе (BigData)
Base.query = session.query_property()

from models import *
Base.metadata.create_all(bind=engine) # создаст схему бд после запуска app


@app.route('/',methods = ['GET']) 
def get_data(): # метод приложения на flask позволяет обратабывать запросы к серверу 
    '''
    возврат данных из базы
    '''
    bigdata = BigData.query.all() # данные полученные из БД с помощью query нельзя сразу вернуть в виде json т.к. это список экз.класса
    serialized = []
    for bigdata in bigdata:
        serialized.append({
            'id': bigdata.id,
            'name': bigdata.name,
            'volume': bigdata.volume})
    return jsonify(serialized)

#@app.route('/',methods=['POST'])
#def add_data():
#    new_one = BigData(**request.json)
#    session.add(new_one)
#    session.commit()
#    serialized = {
#        'id':new_one.id,
#        'name':new_one.name,
#        'volume':new_one.volume}
#    return jsonify(serialized)

@app.route('/<int:lfn>', methods=['POST'])
def findnumber(lfn):
    try:
        path = 'D:\\sber\\Problem2\\'
        files = glob.glob(path + "*.csv")
        while len(files) != 0:
            name = files.pop()
            with open(name,'r') as current_csv:
                global_count = 0
                for row in current_csv:
                    t = len(row)
                    global_count += row.count(str(lfn))
            new_one = BigData(name = name,volume = global_count)
            session.add(new_one)
            session.commit()
    except Exception as e:
        logger.warning(f'Entered wrong data!')
        return {'message': str(e)}, 400
    return 'Ok!'
    

@app.route('/<int:tutorial_id>',methods=['PUT'])
def update_table(tutorial_id):
    item = BigData.query.filter(BigData.id == tutorial_id).first()
    params  = request.json
    if not item:
        return{'message': 'No data with such id'}, 400
    for key, value in params.items():
        setattr(item,key,value)
    session.commit()
    serialized = {
        'id':new_one.id,
        'name':new_one.name,
        'volume':new_one.volume}
    return serialized

@app.route('/<int:tutorial_id>',methods=['DELETE'])
def delete_data(tutorial_id):
    item = BigData.query.filter(BigData.id == tutorial_id).first()
    if not item:
        return{'message': 'No data with such id'}, 400
    session.delete(item)
    session.commit()
    return '', 204

@app.teardown_appcontext
def shutdown_request(exception=None):
    session.remove()



if __name__ == '__main__':
    app.run()