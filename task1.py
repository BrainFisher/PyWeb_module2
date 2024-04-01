import datetime
import calendar


class PersonalAssistant:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}! How can I assist you today?")

    def show_date(self):
        today = datetime.date.today()
        print(f"Today's date is {today.strftime('%B %d, %Y')}.")

    def show_time(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"The current time is {current_time}.")

    def show_calendar(self, year, month):
        cal = calendar.month(year, month)
        print(f"Here's the calendar for {
              calendar.month_name[month]} {year}:\n")
        print(cal)


def main():
    name = input("Please enter your name: ")
    assistant = PersonalAssistant(name)
    assistant.greet()

    while True:
        print("\nMenu:")
        print("1. Show today's date")
        print("2. Show current time")
        print("3. Show calendar")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            assistant.show_date()
        elif choice == "2":
            assistant.show_time()
        elif choice == "3":
            year = int(input("Enter the year: "))
            month = int(input("Enter the month (1-12): "))
            assistant.show_calendar(year, month)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
