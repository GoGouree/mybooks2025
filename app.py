from flask import Flask, render_template

app = Flask(__name__)

# Route for home page
@app.route('/')
def home():
    books = ['Love & Math', 'Underground Railroad', 'Book 3']  # List of books
    return render_template('index.html', books=books)

# Route for book details
@app.route('/book/<title>')
def book_detail(title):
    details = {
        'Love & Math': {'author': 'Edward Frenkel', 'summary': 'Summary of bgh'},
        'Underground Railroad': {'author': 'Colson Whitehead', 'summary': 'Summary of Book 2'},
        'Book 3': {'author': 'Author 3', 'summary': 'Summary of Book 3'},
    }
    book_info = details.get(title, 'Book not found')
    return render_template('book_detail.html', title=title, book_info=book_info)

if __name__ == '__main__':
    app.run(debug=True)
