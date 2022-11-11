from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.post import Post

@app.route('/createPost', methods=['POST'])
def createPost():
    data = {
        'content': request.form['content'],
        'user_id': session['user_id']
    }
    Post.create_post(data)
    return redirect('/')

@app.route('/like/<int:id>')
def addLike(id):
    data = {
        'post_id': id,
        'user_id': session['user_id']
    }
    Post.addLike(data)
    return redirect(request.referrer)

@app.route('/unlike/<int:id>')
def removeLike(id):
    data = {
        'post_id': id,
        'user_id': session['user_id']
    }
    Post.removeLike(data)
    return redirect(request.referrer)