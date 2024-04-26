from flask import Flask,render_template,request,redirect,url_for,session
app=Flask(__name__)

Student_list = [{"Name":"Deva","Age":21 ,"Roll_NO": 101, "Marks":[90,75,80,98,75]},
            {"Name":"Eswar","Age":24 ,"Roll_NO": 102, "Marks":[90,75,80,98,65]},
            {"Name":"Siva","Age":23 ,"Roll_NO": 103, "Marks":[90,75,80,78,99]},
            {"Name":"Ruban","Age":24 ,"Roll_NO": 104, "Marks":[94,75,80,88,35]},
            {"Name":"Kiruba","Age":22 ,"Roll_NO": 105, "Marks":[70,85,80,98,35]},   
            {"Name":"Halith","Age":25 ,"Roll_NO": 106, "Marks":[90,75,85,98,35]},
            {"Name":"Thenmozhi","Age":23 ,"Roll_NO": 107, "Marks":[80,98,35,90,75]}
            ]
usr_name='Kirubakaran'
Password='Kiruba1359'

def isloggedin():
    return usr_name,session

app.secret_key='1359'

@app.route('/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        
        user_name=request.form['name']
        password=request.form['password']  
        
        if user_name==usr_name and password==Password :
            session['usr_name']=user_name 
            return redirect(url_for('table'))
        else:
            return 'Invalid'
        
    return render_template('login.html')

@app.route('/logout/')
def logout():
    session.pop("usr_name",None)
    return redirect(url_for('login'))

@app.route('/table')
def table():
    
    return render_template('index.html',data=Student_list)


@app.route('/add',methods=['GET','POST'])
def add():
    if request.method=='POST':
        
       name=request.form['Name']
       age=request.form['Age']
       roll_no=request.form['Roll_NO']
       tam=request.form['tamil']
       eng=request.form['english']
       math=request.form['math']
       sci=request.form['science']
       ss=request.form['social']
       
       marks_list=[tam,eng,math,sci,ss]
       
       user_dict={'Name':name,
                  'Age':age,
                  'Roll_NO':roll_no,
                  'Marks':marks_list}
       
       Student_list.append(user_dict)
       return redirect(url_for('table'))
       
    return render_template('add.html',data=Student_list)

@app.route('/edit/<string:id>',methods=['GET','POST'])
def edit(id):
    if request.method=='POST':
        
        name=request.form.get('Name')
        age=request.form.get('Age')
        roll_no=request.form.get('Roll_NO')
        tam=request.form.get('tamil')
        eng=request.form.get('english')
        math=request.form.get('math')
        sci=request.form.get('science')
        soci=request.form.get('social')
        
        edit_dict=Student_list[int(id)-1]
        
        mark_list=[tam,eng,math,sci,soci]
        
        edit_dict['Name']=name
        edit_dict['Age']=age
        edit_dict['Roll_NO']=roll_no
        edit_dict['Marks']=mark_list

        return redirect(url_for('table'))
    
    edit_list=Student_list[int(id)-1]
    return render_template('edit.html',form_data=edit_list)

@app.route('/delete/<string:id>',methods=['GET','POST'])
def delete(id):
    
    Student_list.pop(int(id)-1)
    
    return redirect(url_for('table'))

if __name__=='__main__':
    app.run(debug=True)