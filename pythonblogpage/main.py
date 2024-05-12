from flask import Flask, render_template
import requests
from post import Post
app = Flask(__name__)

posts=requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objs = []

for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objs.append(post_obj)

# @app.route('/')
# def home():
#     return render_template("index.html",blog_posts=post_objs)


@app.route("/post/<int:index>")
def read(index):
    req_post=None
    for blogpost in post_objs:
        if blogpost.id == index:
            req_post=blogpost
    return render_template("post.html",post=req_post)

if __name__ == "__main__":
    app.run(debug=True)
