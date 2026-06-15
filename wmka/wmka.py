from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    year: int

class BookManager:
    def __init__(self) -> None:
        self.books: list[Book] = []
    
    def add_book(self) -> None:
        print("\n--- Axali wignis damateba ---")
        title = self._get_valid_text("satauri: ")
        author = self._get_valid_text("avtori: ")
        year = self._get_valid_year("weli: ")
        self.books.append(Book(title, author, year))
        print("wigni warmatebiT damata!")

    def show_all(self) -> None:
        print("\n--- wignebis sia ---")
        if not self.books:
            print("biblioteka carielia.")
            return
        for i, b in enumerate(self.books, 1):
            print(f"{i}. {b.title} - {b.author} ({b.year})")

    def search(self) -> None:
        print("\n--- wignis zebna ---")
        query = self._get_valid_text("satauris nawili: ").lower()
        results = [b for b in self.books if query in b.title.lower()]
        
        if not results:
            print("wigni ver moizebna.")
        else:
            for i, b in enumerate(results, 1):
                print(f"{i}. {b.title} - {b.author} ({b.year})")
    
    def _get_valid_text(self, prompt: str) -> str:
        while True:
            text = input(prompt).strip()
            if text: return text
            print("shecdoma: veli ar unda iyos carieli!")

    def _get_valid_year(self, prompt: str) -> int:
        while True:
            val = input(prompt)
            if val.isdigit() and 1450 <= int(val) <= 2026:
                return int(val)
            print("shecdoma: sheiyvaneT validuri weli (1450-2026)!")

def run_menu():
    manager = BookManager()
    while True:
        print("\n1. damateba | 2. sia | 3. dzebna | 4. gasvla")
        choice = input("airchiet: ")
        
        if choice == "1": manager.add_book()
        elif choice == "2": manager.show_all()
        elif choice == "3": manager.search()
        elif choice == "4": break
        else: print("araswori archevani!")

if __name__ == "__main__":
    run_menu()