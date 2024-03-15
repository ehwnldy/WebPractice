from flask import Flask, render_template,request
import datetime
from flask import Flask,render_template, request, current_app, redirect, url_for
from sqlalchemy import create_engine, text


app = Flask(__name__)


@app.route('/')
def index():
  now = datetime.datetime.now()
  print(now)
  dict = { '제목': '안녕하세요', '작성자' : '홍길동', '작성일' : '2022-11-25', '조회수': 30}
  return render_template('index.html' , current_time= now , score = 40 ,result = dict)
  
  

@app.route('/education')
def education():
  return render_template('education.html')

@app.route('/experience')
def experience():
  return render_template('experience.html')

@app.route('/guestbook')
def guestbook():
  return render_template('guestbook.html')

@app.route('/skills')
def skills():
  return render_template('skills.html')

@app.route('/layout')
def layout():
  return render_template('layout.html')



def get_list():
    list = current_app.database.execute(text("""
        SELECT 
            id,
            username,
            userno,
            contents
        FROM guest_book
    """)).fetchall()
    print(list)
    
    return list

@app.route('/insert', methods=['POST'])
def insert_book():
    
    username = request.form['username']
    userno = request.form['userno']
    contents = request.form['contents']

    insertDict = {}
    insertDict['username'] = username
    insertDict['userno'] = userno
    insertDict['contents'] = contents
    
    print(insertDict)
    
    id = current_app.database.execute(text("""
        INSERT INTO guest_book (
            username,
            userno,
            contents
        ) VALUES (
            :username,
            :userno,
            :contents
        )
    """), insertDict).lastrowid
    print(id)
    return redirect(url_for('guest'))

@app.route('/login',methods = ["POST", "GET"])
def login():
  req_method = request.method
  if req_method =='GET':
    return render_template('login.html',result =None)
  elif req_method == 'POST':
    # id,password 검증을 통해 로그인 성공여부 리턴
    id = request.form['id']
    password = request.form['password']
    result = ''
    if id == 'admin' and password == 'test':
      result = '로그인 성공'
    else:
      result = '로그인 실패'
    return render_template('login.html', result =result)
  
  
if __name__ == '__main__':
  app.run(debug=True,port=5002)