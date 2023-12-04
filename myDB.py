import pymysql

def getData():
    db = pymysql.connect(
        user='root',
        passwd='1234',
        host='localhost',
        db='project'
    )
    cursor = db.cursor()

    sql = f"""
        SELECT * FROM project.board;
        """
    cursor.execute(sql)
    rows = cursor.fetchall()

    data_list = []
    for i in range(len(rows)):
        data = {
            'id': rows[i][0],
            'name': rows[i][1],
            'title': rows[i][2],
            'view': rows[i][3],
            'date': rows[i][4],
            'pwd': rows[i][5],
            'content': rows[i][6]
            }
        data_list.append(data)

    db.commit()
    db.close()

    return data_list

def getViewDate(board_id):
    db = pymysql.connect(
        user='root',
        passwd='1234',
        host='localhost',
        db='project'
    )
    cursor = db.cursor()

    sql = f"""
        SELECT * FROM project.board where board_id=%s;
        """
    cursor.execute(sql, (board_id))
    rows = cursor.fetchall()

    num = rows[0][0]
    name = rows[0][1]
    title = rows[0][2]
    view = rows[0][3]
    date = rows[0][4]
    pwd = rows[0][5]
    content = rows[0][6]
        
    db.commit()
    db.close()

    return num, name, title, view, date, content, pwd

def saveData(title, name, pwd, content):
    db = pymysql.connect(
        user='root',
        passwd='1234',
        host='localhost',
        db='project'
    )
    cursor = db.cursor()

    sql = f"""
        INSERT INTO `project`.`board` (`name`, `title`, `date`, `pwd`, `content`) VALUES (%s, %s, sysdate(), %s, %s);
        """
    cursor.execute(sql, (name, title, pwd, content))
        
    db.commit()
    db.close()
    
def updateData(num, title, name, content):
    db = pymysql.connect(
        user='root',
        passwd='1234',
        host='localhost',
        db='project'
    )
    cursor = db.cursor()

    sql = f"""
        update `project`.`board` set name=%s, title=%s, content=%s where board_id=%s;
        """
    cursor.execute(sql, (name, title, content, num))
        
    db.commit()
    db.close()
    
def updateView(num):
    db = pymysql.connect(
        user='root',
        passwd='1234',
        host='localhost',
        db='project'
    )
    cursor = db.cursor()

    sql = f"""
        update `project`.`board` set view=view+1 where board_id = %s;
        """
    cursor.execute(sql, (num))
        
    db.commit()
    db.close()