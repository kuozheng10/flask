from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__) #__name__代表目前執行的模組
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

def __repr__(self):
    return 'Blog post ' + str(self.id)    



# '/'代表網站的根目錄
@app.route('/')#函式的裝飾(Decorator): 以函式為基礎，提供附加的功能
def index():
    return render_template('index.html')

@app.route('/posts', methods=['GET', 'POST'])
def posts():

    if request.method == 'POST':
        post_title = request.form['title']
        post_author = request.form['author']
        post_content = request.form['content']
        new_post = BlogPost(title=post_title, content=post_title, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:    
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('posts.html', posts=all_posts)

@app.route('/home/users/<string:name>/posts/<int:id>') #代表我們要處理的網站路徑
def hello(name, id):
    return 'Hello, ' + name + ', your id is : ' + str(id)

@app.route('/onlyget', methods=['GET'])
def get_req():
    return 'You an only get this webpga 4'


if __name__ == '__main__':#如果以主程式執行
    app.run(debug=True) #立刻啟動伺服器