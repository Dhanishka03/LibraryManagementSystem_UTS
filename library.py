# Library Management System

# Book details
books = [
    {
        "Book Name": "Python Programming",
        "Author": "John Smith",
        "Price": 450
    },
    {
        "Book Name": "Data Science Basics",
        "Author": "Andrew Kumar",
        "Price": 550
    },
    {
        "Book Name": "Machine Learning",
        "Author": "Tom Mitchell",
        "Price": 600
    },
    {
        "Book Name": "Artificial Intelligence",
        "Author": "Stuart Russell",
        "Price": 750
    }
]


# Function to display books
def display_books():
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("\nAvailable Books:\n")

    for book in books:
        print("Book Name :", book["Book Name"])
        print("Author    :", book["Author"])
        print("Price     : ₹", book["Price"])
        print("-" * 40)


# Main program
display_books()