import requests

# Ekstraksi data dari API
query = "Data Engineering"
url = f"https://openlibrary.org/search.json?q={query.replace(' ', '+')}"
response = requests.get(url)
data = response.json()

# Pembersihan dan Transformasi Data
books = []

for book in data['docs'][:10]:
    authors = book.get('author_name') or []
    author_name = authors[0] if authors else None

    books.append({
        'title': book.get('title'),
        'author_name': author_name,
        'first_publish_year': book.get('first_publish_year')
    })

for book in books:
    print(book)
    print('=====')