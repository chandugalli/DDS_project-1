# ------------------------------
# E-Library Book Management System
# ------------------------------

class Book:
    """A single book node in the linked list"""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
        self.next = None


class Inventory:
    """Linked list for managing book inventory"""
    def __init__(self):
        self.head = None

    def add_book(self, title, author):
        new_book = Book(title, author)
        if not self.head:
            self.head = new_book
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_book
        print(f"📚 Added: {title} by {author}")

    def display_books(self):
        if not self.head:
            print("⚠️ No books in the library.")
            return
        print("\n--- 📖 Library Inventory ---")
        temp = self.head
        while temp:
            status = "✅ Available" if temp.available else "❌ Borrowed"
            print(f"{temp.title} by {temp.author} - {status}")
            temp = temp.next

    def find_book(self, title):
        temp = self.head
        while temp:
            if temp.title.lower() == title.lower():
                return temp
            temp = temp.next
        return None

    def search(self, keyword):
        print(f"\n🔍 Search results for '{keyword}':")
        temp = self.head
        found = False
        while temp:
            if keyword.lower() in temp.title.lower() or keyword.lower() in temp.author.lower():
                status = "✅ Available" if temp.available else "❌ Borrowed"
                print(f"{temp.title} by {temp.author} - {status}")
                found = True
            temp = temp.next
        if not found:
            print("⚠️ No matches found.")


class Action:
    """Action record for undo stack"""
    def __init__(self, action_type, book):
        self.action_type = action_type  # "borrow" or "return"
        self.book = book


class ELibrary:
    def __init__(self):
        self.inventory = Inventory()
        self.undo_stack = []

    def borrow_book(self, title):
        book = self.inventory.find_book(title)
        if not book:
            print("⚠️ Book not found.")
            return
        if not book.available:
            print("❌ Book is already borrowed.")
            return
        book.available = False
        self.undo_stack.append(Action("borrow", book))
        print(f"📕 Borrowed: {book.title}")

    def return_book(self, title):
        book = self.inventory.find_book(title)
        if not book:
            print("⚠️ Book not found.")
            return
        if book.available:
            print("⚠️ Book was not borrowed.")
            return
        book.available = True
        self.undo_stack.append(Action("return", book))
        print(f"📗 Returned: {book.title}")

    def undo(self):
        if not self.undo_stack:
            print("⚠️ Nothing to undo.")
            return
        action = self.undo_stack.pop()
        if action.action_type == "borrow":
            action.book.available = True
            print(f"↩️ Undo: Borrow undone for '{action.book.title}'")
        elif action.action_type == "return":
            action.book.available = False
            print(f"↩️ Undo: Return undone for '{action.book.title}'")


# ------------------------------
# Main Console Program
# ------------------------------
def main():
    library = ELibrary()

    # Preload some books
    library.inventory.add_book("The Alchemist", "Paulo Coelho")
    library.inventory.add_book("1984", "George Orwell")
    library.inventory.add_book("Python Programming", "John Zelle")

    while True:
        print("\n=== 📚 E-Library Book Management ===")
        print("1) Display all books")
        print("2) Borrow a book")
        print("3) Return a book")
        print("4) Undo last action")
        print("5) Search book by title/author")
        print("0) Exit")

        choice = input("Choose option: ").strip()

        if choice == "0":
            print("👋 Exiting E-Library. Goodbye!")
            break
        elif choice == "1":
            library.inventory.display_books()
        elif choice == "2":
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)
        elif choice == "3":
            title = input("Enter book title to return: ")
            library.return_book(title)
        elif choice == "4":
            library.undo()
        elif choice == "5":
            keyword = input("Enter keyword (title/author): ")
            library.inventory.search(keyword)
        else:
            print("⚠️ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
