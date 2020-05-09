from datetime import datetime
from app import db

class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    bio = db.Column(db.String(255))
    image_file = db.Column(db.String())
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
        <--->

class Post(db.Model):
    __tablename__='post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category = db.Column(db.String)
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    comments = db.relationship('Comment', backref = 'post', lazy = 'dynamic')

    def get_comments(self):
      post = Post.query.filter_by(id=self.id).first()
      comments = Comment.query.filter_by(id = post.id).all()
      return comments

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}','{self.category})"

class Comment(db.Model):
  __tablename__='comments'
  id = db.Column(db.Integer,primary_key=True)
  post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  content = db.Column(db.String)
  
  def save_comment(self):
    db.session.add(self)
    db.session.commit()

  def __repr__(self):
    return f'User {self.content}'  


