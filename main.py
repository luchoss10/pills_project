from enum import Enum
from models.day import DayRecord
from models.pill import Pill
from models.user import User

from storage_modules import json_file_storage

class SelectOption(Enum):
    YES = 1
    NO = 2
    EXIT = 3

class MenuOptions(Enum):
    MANAGE_PILLS = 1
    MANAGE_DAY_RECORD = 2

class ManagePillsOptions(Enum):
    ADD_PILL = 1
    DELETE_PILL = 2
    MODIFY_PILL = 3
    SHOW_PILLS = 4

class ManageDayRecordOptions(Enum):
    ADD_DAY_RECORD = 1
    DELETE_DAY_RECORD = 2
    MODIFY_DAY_RECORD = 3
    SHOW_DAY_RECORD = 4
    CLOSE = 5

def start_app_protocol() -> User:
    print("-" * 50)
    print(f"Hello Welcome to Pill Tracker")
    print("-" * 50)
    print("Pill Tracker is a program to help you keep track of your pills")
    print("You can gestion your pills and your daily register")

    print("-" * 50)
    print("Is your first time using Pill Tracker?")


    while True:        
        option = input("Yes/No: ")
        if option.lower() in ["yes", "no"]:
            break
        print("Please select a valid option")

    
    user = User("Generic User", 99)
    
    if not option.lower() == "yes":
        print("Welcome back!")
        # Implementate a search user function
        # user =  get_user()
        # user = User(name, age)
        return user

    if option.lower() == "yes":
        print("Let's start by creating your user profile!")
        name = input("Please enter your name: ")
        age = int(input("Please enter your age: "))
        user = User(name, age)
        print(f"Welcome {user.name}!")
        
        return user


def manage_pills(user: User):
    while True:
        print("-" * 50)
        print("Please select an option")
        print("1. Add a new pill")
        print("2. Delete a pill")
        print("3. Modify a pill")
        print("4. Show all pills")
        print("5. Exit")

        option = input("Option: ")

        if option == "1":
            print("Please enter the pill information")
            name = input("Name: ")
            measure = input("Measure: ")
            description = input("Description: ")
            frequency_day = input("Frequency day: ")
            pill = Pill(name, measure, description, frequency_day)
            user.add_pill(pill)
        elif option == "2":
            print("Please select the pill you want to delete")
            pills = user.get_pills()
            for i, pill in enumerate(pills):
                print(f"{i}. {pill.name}")
            option = input("Option: ")
            user.delete_pill(pills[int(option)])
        elif option == "3":
            print("Please select the pill you want to modify")
            pills = user.get_pills()
            for i, pill in enumerate(pills):
                print(f"{i}. {pill.name}")
            option = input("Option: ")
            pill = pills[int(option)]
            user.delete_pill(pill)
            print("Please enter the new pill information")
            name = input("Name: ")
            measure = input("Measure: ")
            description = input("Description: ")
            frequency_day = input("Frequency day: ")
            pill.change_name(name)
            pill.change_measure(measure)
            pill.change_description(description)
            pill.change_frequency_day(frequency_day)
            user.add_pill(pill)
        elif option == "4":
            print("Your pills are:")
            pills = user.get_pills()
            for pill in pills:
                print(pill)
        elif option == "5":
            print("Returning to main menu")
            break
        else:
            print("Please select a valid option")


def manage_daily_register(user: User):
    while True:
        print("-" * 50)
        print("Please select an option")
        print("1. Add a new day register")
        print("2. Delete a day register")
        print("3. Modify a day register")
        print("4. Show all day register")
        print("5. Exit")

        option = input("Option: ")

        if option == "1":
            print("Please enter the day register information")
            date = input("Date (form YYYY-MM-DD): ")
            note = input("Note: ")
            pill_list = []
            while True:
                print("Please select the pills you took today")
                pills = user.get_pills()
                for i, pill in enumerate(pills):
                    print(f"{i}. {pill.name}")
                option = input("Option: ")
                pill_list.append(pills[int(option)])
                print("Do you want to add another pill?")
                option = input("Yes/No: ")
                if option.lower() == "no":
                    break
            day_record = DayRecord(date, pill_list, note)
            user.add_day_record(day_record)
        elif option == "2":
            print("Please select the day register you want to delete")
            day_records = user.get_history()
            # split_step = 10
            for i, day_record in enumerate(day_records):
                print(f"{i}. {day_record.date}")
            option = input("Option: ")
            user.delete_day_record(day_records[int(option)])
        elif option == "3":
            print("Please select the day register you want to modify")
            day_records = user.get_history()
            for i, day_record in enumerate(day_records):
                print(f"{i}. {day_record.date}")
            option = input("Option: ")
            day_record = day_records[int(option)]
            user.delete_day_record(day_record)
            print("Please enter the new day register information")
            date = input("Date: (form YYYY-MM-DD):")
            note = input("Note: ")
            pill_list = []
            while True:
                print(f"Please select the pills you took the day: {date}")
                pills = user.get_pills()
                for i, pill in enumerate(pills):
                    print(f"{i}. {pill.name}")
                option = input("Option: ")
                pill_list.append(pills[int(option)])
                print("Do you want to add another pill?")
                option = input("Yes/No: ")
                if option.lower() == "no":
                    break
            day_record = DayRecord(date, pill_list, note)
            user.add_day_record(day_record)
        elif option == "4":
            print("Your day register are:")
            day_records = user.get_history()
            for day_record in day_records:
                print(day_record)
        elif option == "5":
            print("Returning to main menu")
            break
        else:
            print("Please select a valid option")


def main():
    pill_l = Pill("Losartan", 50)
    pill_a = Pill("Atorvastatina", 20, "Tomar dia de por medio")

    user = start_app_protocol()

    while True:
        print("-" * 50)
        print("Please select an option")
        print(f"{MenuOptions.MANAGE_PILLS.value}. Manage pills")
        print(f"{MenuOptions.MANAGE_DAY_RECORD.value}. Manage daily register")
        print(f"{SelectOption.EXIT.value}. Exit")

        option = input("Option: ")
        print(f"Option selected: {option}")

        if option == MenuOptions.MANAGE_PILLS.value:
            manage_pills(user)
        elif option == MenuOptions.MANAGE_DAY_RECORD.value:
            manage_daily_register(user)
        elif option == SelectOption.EXIT.value:
            print("Thanks for using Pill Tracker")
            break
        else:
            print("Please select a valid option")

    record_history = []

    for i in range(1, 11):
        record_history.append(DayRecord(f"2021-09-0{i}", [pill_l, pill_a]))

    print(record_history)


if __name__ == "__main__":
    main()
