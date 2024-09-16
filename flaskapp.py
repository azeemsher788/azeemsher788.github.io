from flask import Flask, render_template
from data import Post

app = Flask(__name__)
post = Post()

@app.route('/')
def home():
    return render_template(
        template_name_or_list="index.html",
    )

@app.route('/blog')
def blogs_main():
    return render_template(
        template_name_or_list="blogs.html",
        title=post.title,
        subtitle=post.subtitle,
        body=post.body,
    )
@app.route('/blog/<int:num>')
def get_blog(num):
    return render_template(
        template_name_or_list="post.html",
        title=post.title[num-1],
        body=post.body[num-1],
        no_animation = True, # Pass a flag to indicate the post is open
    )

@app.route('/web_app')
def web_app_open():
    return render_template(
        template_name_or_list="web_app.html",
    )

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=80)
    app.run(debug=True)