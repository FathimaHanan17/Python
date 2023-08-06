import csv

def create_book_genre_dict(books):
    book_genre_dict = {}
    for book in books:
        genre = book["Genre"]
        if genre not in book_genre_dict:
            book_genre_dict[genre] = []
        book_genre_dict[genre].append(book)
    return book_genre_dict

def recommend_books_by_genre(books, genre, num_recommendations=10):
    recommended_books = []
    for book in books:
        if book["Genre"] == genre:
            recommended_books.append(book)

    if not recommended_books:
        return []

    recommended_books.sort(key=lambda x: x["User Rating"], reverse=True)
    return recommended_books[:num_recommendations]

def recommend_books_by_author(books, author_name, num_recommendations=10):
    recommended_books = []
    for book in books:
        if author_name.lower() in book["Author"].lower():
            recommended_books.append(book)

    if not recommended_books:
        return []

    recommended_books.sort(key=lambda x: x["User Rating"], reverse=True)
    return recommended_books[:num_recommendations]


    # Read data from the CSV file
books_data = []
with open("books.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
         books_data.append(row)
book_genre_dict = create_book_genre_dict(books_data)

while True:
    print("1. Search by Book Title")
    print("2. Search by Author Name")
    print("3. Exit")

    choice = int(input("Enter your choice (1/2/3): "))
 
    if choice == 1:
       book_title = input("Enter the Book Title: ")
       found_books = [book for book in books_data if book["Book Title"].lower() == book_title.lower()]
       if found_books:
          genre = found_books[0]["Genre"]
          recommended_books = recommend_books_by_genre(book_genre_dict[genre], genre)
          print("\nRecommended books with the same genre:")
          for i, book in enumerate(recommended_books, 1):
              print(f"{i}. {book['Book Title']} by {book['Author']} (User Rating: {book['User Rating']})")
       else:
          print("Book not found.")

    elif choice == 2:
        author_name = input("Enter the Author Name: ")
        recommended_books = recommend_books_by_author(books_data, author_name)
        if recommended_books:
            print("\nRecommended books by the same author:")
            for i, book in enumerate(recommended_books, 1):
                print(f"{i}. {book['Book Title']} (User Rating: {book['User Rating']})")
        else:
            print("Author not found.")

    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")