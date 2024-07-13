class CinemaBooking:
    def __init__(self):
        self.movies = {
            "Фільм 1": ["10:00", "13:00", "16:00", "19:00"],
            "Фільм 2": ["11:00", "14:00", "17:00", "20:00"],
            "Фільм 3": ["12:00", "15:00", "18:00", "21:00"]
        }
        self.seats = [False] * 10

    def display_menu(self):
        print("\n--- Сервіс купівлі квитків в кіно ---")
        print("1. Переглянути розклад сеансів")
        print("2. Забронювати квиток")
        print("3. Купити квиток")
        print("4. Вихід")

    def display_schedule(self):
        print("\n--- Розклад сеансів ---")
        for movie, times in self.movies.items():
            print(f"{movie}: {', '.join(times)}")

    def display_seats(self):
        print("\n--- Доступні місця ---")
        for i in range(10):
            status = "вільне" if not self.seats[i] else "зайняте"
            print(f"Місце {i+1}: {status}")

    def book_or_buy_ticket(self, action):
        movie = input("Оберіть фільм: ")
        if movie not in self.movies:
            print("Невірний вибір фільму.")
            return

        time = input("Оберіть час сеансу: ")
        if time not in self.movies[movie]:
            print("Невірний вибір часу.")
            return

        self.display_seats()
        seat_number = int(input("Оберіть номер місця (1-10): ")) - 1
        if seat_number < 0 or seat_number >= 10:
            print("Невірний вибір місця.")
            return
        if self.seats[seat_number]:
            print("Це місце вже зайняте.")
            return

        self.seats[seat_number] = True
        print(f"Місце {seat_number+1}: {action} на {movie} о {time}.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Оберіть опцію: ")

            if choice == "1":
                self.display_schedule()
            elif choice == "2":
                self.book_or_buy_ticket("Заброньовано")
            elif choice == "3":
                self.book_or_buy_ticket("Куплено")
            elif choice == "4":
                print("Дякуємо за використання сервісу!")
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    app = CinemaBooking()
    app.run()

