from enum import Enum
from models.day import DayRecord
from models.pill import Pill
from models.user import User

from storage_modules import json_file_storage

from utils import get_logger

logger = get_logger(__name__, "logs")

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
    CLOSE = 5

class ManageDayRecordOptions(Enum):
    ADD_DAY_RECORD = 1
    DELETE_DAY_RECORD = 2
    MODIFY_DAY_RECORD = 3
    SHOW_DAY_RECORD = 4
    CLOSE = 5

def start_app_protocol() -> User:
    logger.info("-" * 50)
    logger.info("Hello Welcome to Pill Tracker")
    logger.info("-" * 50)
    logger.info("Pill Tracker is a program to help you keep track of your pills")
    logger.info("You can gestion your pills and your daily register")

    logger.info("-" * 50)
    logger.info("Is your first time using Pill Tracker?")


    while True:        
        option = input("Yes/No: ")
        if option.lower() in ["yes", "no"]:
            break
        logger.info("Please select a valid option")

    
    user = User("Generic User", 99)
    
    if not option.lower() == "yes":
        logger.info("Welcome back!")
        # Implementate a search user function
        # user =  get_user()
        # user = User(name, age)
        return user

    if option.lower() == "yes":
        logger.info("Let's start by creating your user profile!")
        name = input("Please enter your name: ")
        age = int(input("Please enter your age: "))
        user = User(name, age)
        logger.info(f"Welcome {user.name}!")
        
        return user


def manage_pills(user: User):
    while True:
        logger.info("-" * 50)
        logger.info("Please select an option")
        logger.info("1. Add a new pill")
        logger.info("2. Delete a pill")
        logger.info("3. Modify a pill")
        logger.info("4. Show all pills")
        logger.info("5. Exit")

        option = int(input("Option: "))

        if option == ManagePillsOptions.ADD_PILL.value:
            logger.info("Please enter the pill information")
            name = input("Name: ")
            measure = input("Measure: ")
            description = input("Description: ")
            frequency_day = input("Frequency day: ")
            pill = Pill(name, measure, description, frequency_day)
            user.add_pill(pill)
        elif option == ManagePillsOptions.DELETE_PILL.value:
            logger.info("Please select the pill you want to delete")
            pills = user.get_pills()
            for i, pill in enumerate(pills):
                logger.info(f"{i}. {pill.name}")
            option = input("Option: ")
            user.delete_pill(pills[int(option)])
        elif option == ManagePillsOptions.MODIFY_PILL.value:
            logger.info("Please select the pill you want to modify")
            pills = user.get_pills()
            for i, pill in enumerate(pills):
                logger.info(f"{i}. {pill.name}")
            option = input("Option: ")
            pill = pills[int(option)]
            user.delete_pill(pill)
            logger.info("Please enter the new pill information")
            name = input("Name: ")
            measure = input("Measure: ")
            description = input("Description: ")
            frequency_day = input("Frequency day: ")
            pill.change_name(name)
            pill.change_measure(measure)
            pill.change_description(description)
            pill.change_frequency_day(frequency_day)
            user.add_pill(pill)
        elif option == ManagePillsOptions.SHOW_PILLS.value:
            logger.info("Your pills are:")
            pills = user.get_pills()
            for pill in pills:
                logger.info(pill)
        elif option == ManagePillsOptions.CLOSE.value:
            logger.info("Returning to main menu")
            break
        else:
            logger.info("Please select a valid option")


def manage_daily_register(user: User):
    while True:
        logger.info("-" * 50)
        logger.info("Please select an option")
        logger.info(f"{ManageDayRecordOptions.ADD_DAY_RECORD.value}. Add a new day register")
        logger.info(f"{ManageDayRecordOptions.DELETE_DAY_RECORD.value}. Delete a day register")
        logger.info(f"{ManageDayRecordOptions.MODIFY_DAY_RECORD.value}. Modify a day register")
        logger.info(f"{ManageDayRecordOptions.SHOW_DAY_RECORD.value}. Show all day register")
        logger.info(f"{ManageDayRecordOptions.CLOSE.value}. Exit")

        option = int(input("Option: "))

        if option == ManageDayRecordOptions.ADD_DAY_RECORD.value:
            logger.info("Please enter the day register information")
            date = input("Date (form YYYY-MM-DD): ")
            note = input("Note: ")
            pill_list = []
            while True:
                logger.info("Please select the pills you took today")
                pills = user.get_pills()
                for i, pill in enumerate(pills):
                    logger.info(f"{i}. {pill.name}")
                option = int(input("Option: "))
                pill_list.append(pills[option])
                logger.info("Do you want to add another pill?")
                option = input("Yes/No: ")
                if option.lower() == "no":
                    break
            day_record = DayRecord(date, pill_list, note)
            user.add_day_record(day_record)
        elif option == ManageDayRecordOptions.DELETE_DAY_RECORD.value:
            logger.info("Please select the day register you want to delete")
            day_records = user.get_history()
            # split_step = 10
            for i, day_record in enumerate(day_records):
                logger.info(f"{i}. {day_record.date}")
            option = input("Option: ")
            user.delete_day_record(day_records[int(option)])
        elif option == ManageDayRecordOptions.MODIFY_DAY_RECORD.value:
            logger.info("Please select the day register you want to modify")
            day_records = user.get_history()
            for i, day_record in enumerate(day_records):
                logger.info(f"{i}. {day_record.date}")
            option = input("Option: ")
            day_record = day_records[int(option)]
            user.delete_day_record(day_record)
            logger.info("Please enter the new day register information")
            date = input("Date (form YYYY-MM-DD):")
            note = input("Note: ")
            pill_list = []
            while True:
                logger.info(f"Please select the pills you took the day: {date}")
                pills = user.get_pills()
                for i, pill in enumerate(pills):
                    logger.info(f"{i}. {pill.name}")
                option = input("Option: ")
                pill_list.append(pills[int(option)])
                logger.info("Do you want to add another pill?")
                option = input("Yes/No: ")
                if option.lower() == "no":
                    break
            day_record = DayRecord(date, pill_list, note)
            user.add_day_record(day_record)
        elif option == ManageDayRecordOptions.SHOW_DAY_RECORD.value:
            logger.info("Your day register are:")
            day_records = user.get_history()
            for day_record in day_records:
                logger.info(day_record)
        elif option == ManageDayRecordOptions.CLOSE.value:
            logger.info("Returning to main menu")
            break
        else:
            logger.info("Please select a valid option")


def main():
    pill_l = Pill("Losartan", 50)
    pill_a = Pill("Atorvastatina", 20, "Tomar dia de por medio")

    user = start_app_protocol()

    while True:
        logger.info("-" * 50)
        logger.info("Please select an option")
        logger.info(f"{MenuOptions.MANAGE_PILLS.value}. Manage pills")
        logger.info(f"{MenuOptions.MANAGE_DAY_RECORD.value}. Manage daily register")
        logger.info(f"{SelectOption.EXIT.value}. Exit")

        option = int(input("Option: "))
        logger.info(f"Option selected: {option}")

        if option == MenuOptions.MANAGE_PILLS.value:
            manage_pills(user)
        elif option == MenuOptions.MANAGE_DAY_RECORD.value:
            manage_daily_register(user)
        elif option == SelectOption.EXIT.value:
            logger.info("Thanks for using Pill Tracker")
            break
        else:
            logger.info("Please select a valid option")

    record_history = []

    for i in range(1, 11):
        record_history.append(DayRecord(f"2021-09-0{i}", [pill_l, pill_a]))

    logger.info(record_history)


if __name__ == "__main__":
    main()
