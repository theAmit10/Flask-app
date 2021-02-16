from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

posts = {
    0:{
        'post_id': 0,
        'name': 'Amit KP',
        'about': 'Hello my name is Amit ,here i am writing my first Blog'
    }
}

@app.route('/')     # it is only used for the GET method.
def home():
    return render_template('home.jinja2', posts=posts)



@app.route('/post/<int:post_id>')   # /post/0
def post(post_id):
    post = posts.get(post_id)   # if the .get method return None its return none when the post_id did not match.
    if not post: # post will be none if not Found; not None => True
        return render_template('404.html', message=f"A post with id {post_id} was not found..." )
    return render_template('post.html', post=post)  # here the First post is post within the post.html page and the another post is sending data that post.


#    return f"Post {post['name']} , About:\n\n {post['about']} "

#@app.route('/post/form')
#def form():
#   return render_template('form.html')

# localhost:5000/post/form/create?titile=something&content=something esle

# @app.route() is used by only GET method if we want to use it by the POST method than we have to add method=['POST'] method in it
@app.route('/post/create', methods=['GET','POST'])
def create():
    if request == 'POST':
    # name = request.args.get('name')
        name = request.form.get('name')
    # about = request.args.get('about')
        about = request.form.get('about')
        post_id = len(posts)
        posts[post_id] = {'id': post_id, 'name': name , 'about': about}

        return redirect(url_for('post', post_id = post_id))
    return render_template('form.html') # if the request is GET then only it return this



"""
here we are doing both GET and POST in same function 
so we have to remove the action from the form tag.
 <form action="/post/create" method="POST"> 
 then it become
 <form method="POST"> 
"""


if __name__ == '__main__':
    app.run(debug=True)

#app.run(debug=True)