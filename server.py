from flask import Flask, render_template
from myDB import getData, getViewDate, saveData, updateData, updateView
from flask import request

app = Flask(__name__)



@app.route('/')
def home():
    data_list = getData()

    return render_template('index.html', data_list=data_list)

@app.route('/view')
def view():

    data_list = getData()

    return render_template('view.html', data_list=data_list)

@app.route('/write')
def write():

    return render_template('write.html')

@app.route('/edit', methods=['get', 'post'])
def edit():
    if request.method == "POST":
        title = request.form.get("title")
        name = request.form.get("name")
        content = request.form.get("content")
        num = request.form.get("num")
        pwd = request.form.get("pwd")
        
        #조회수 증가 시키기
        updateView(num)
    
        return render_template('edit.html', title=title, name=name, content=content, num=num, pwd=pwd)

@app.route('/gotoview', methods=['get', 'post'])
def gotoview():
    if request.method == "POST":
        board_id = request.form.get("board_id")
        num, name, title, view, date, content, pwd = getViewDate(board_id)

        return render_template('view.html', num=num, name=name, title=title, view=view, date=date, content=content, pwd=pwd)

@app.route('/index')
def index():
    data_list = getData()

    return render_template('index.html', data_list = data_list)

@app.route('/saveWrite', methods=['get', 'post'])
def save_write():
    if request.method == "POST":
        title = request.form.get("title")
        name = request.form.get("name")
        pwd = request.form.get("pwd")
        content = request.form.get("content")
        
        #등록하기
        saveData(title, name, pwd, content)
    
        data_list = getData()
        return render_template('index.html', data_list=data_list)
    
@app.route('/editWrite', methods=['get', 'post'])
def editWrite():
    if request.method == "POST":
        title = request.form.get("title")
        name = request.form.get("name")
        content = request.form.get("content")
        num = request.form.get("num")
        
        #수정하기
        updateData(num, title, name, content) 

        data_list = getData()
        return render_template('index.html', data_list=data_list)


if __name__ == '__main__':
    app.run('0.0.0.0', port=9090, debug=True)