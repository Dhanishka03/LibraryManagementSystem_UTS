# Library Management System

books = [
    {
        "Book Name": "Python Programming",
        "Author": "John Smith",
        "Price": 450,
        "Available": True
    },
    {
        "Book Name": "Data Science Basics",
        "Author": "Andrew Kumar",
        "Price": 550,
        "Available": True
    },
    {
        "Book Name": "Machine Learning",
        "Author": "Tom Mitchell",
        "Price": 600,
        "Available": True
    },
    {
        "Book Name": "Artificial Intelligence",
        "Author": "Stuart Russell",
        "Price": 750,
        "Available": True
    }
]


# Display all books
def display_books():
    print("\n===== AVAILABLE BOOKS =====")

    for book in books:
        print("\nBook Name :", book["Book Name"])
        print("Author    :", book["Author"])
        print("Price     : ₹", book["Price"])

        if book["Available"]:
            print("Status    : Available")
        else:
            print("Status    : Issued")

        print("-" * 40)


# Issue a book
def issue_book():
    book_name = input("\nEnter the book name to issue: ")

    for book in books:
        if book["Book Name"].lower() == book_name.lower():

            if book["Available"]:
                book["Available"] = False
                print("\nBook issued successfully!")
                print("Book Name :", book["Book Name"])
            else:
                print("\nSorry, this book is already issued.")

            return

    print("\nBook not found in the library.")


# Main menu
while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Display Books")
    print("2. Issue Book")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        display_books()

    elif choice == "2":
        issue_book()

    elif choice == "3":
        print("\nThank you for using the Library Management System!")
        break

    else:
        print("\nInvalid choice. Please try again.")
