from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data
posts = [
    {
        'id': 1,
        'title': 'First Post',
        'content': 'This is the content of the first post.'
    },
    {
        'id': 2,
        'title': 'Second Post',
        'content': 'This is the content of the second post.'
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    return render_template('post.html', post=post)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        new_post = {
            'id': len(posts) + 1,
            'title': request.form['title'],
            'content': request.form['content']
        }
        posts.append(new_post)
        return redirect(url_for('index'))
    return render_template('new_post.html')

if __name__ == '__main__':
    app.run(debug=True)
    
<!DOCTYPE html>
<html>
<head>
    <title>My Blog</title>
</head>
<body>
    <h1>My Blog</h1>
    <a href="/new">Create New Post</a>
    <ul>
        {% for post in posts %}
        <li>
            <a href="/post/{{ post.id }}">{{ post.title }}</a>
        </li>
        {% endfor %}
    </ul>
</body>
</html>

<!DOCTYPE html>
<html>
<head>
    <title>{{ post.title }}</title>
</head>
<body>
    <h1>{{ post.title }}</h1>
    <p>{{ post.content }}</p>
    <a href="/">Back to Home</a>
</body>
</html>
<!DOCTYPE html>
<html>
<head>
    <title>Create New Post</title>
</head>
<body>
    <h1>Create New Post</h1>
    <form method="post">
    <label>Title:</label>
<input type="text" name="title" required>
    <br>
        <label>Content:</label>
        <textarea name="content" required></textarea>
     <br>
    <button type="submit">Create Post</button>
    </form>
    <a href="/">Back to Home</a>
</body>
