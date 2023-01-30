from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/hi')
def hai():
    return render_template('hai.html')

@FAI.route('/macha')
def hello():
    return render_template('hello.html')

if __name__=='__main__':
    FAI.run(debug=True)