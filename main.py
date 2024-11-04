from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store
books = []

# Home route to display books
@app.route('/')
def index():
    return render_template('index.html', books=books)

# Route to add a book
@app.route('/add', methods=['POST'])
def add_book():
    title = request.form.get('title')
    author = request.form.get('author')
    if title and author:
        books.append({"title": title, "author": author})
    return redirect(url_for('index'))

# Route to delete a book by title
@app.route('/delete/<string:title>', methods=['POST'])
def delete_book(title):
    global books
    books = [book for book in books if book['title'] != title]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
