from pill import Pill
from day import Day
from datetime import datetime


def get_days(first_date:datetime=None, last_date:datetime=None)->list[Day]:
    """Return pIlls Objects from a range of dates.

    Args:
        first_date (datetime, optional): First date of range to search. Defaults to None.
        last_date (datetime, optional): Last date of range to search. Defaults to None.

    Returns:
        list[Day]: List of days objects from the specified range.
    """

    # Make the data classes for connect a database in mysql
    pass

def get_pills(day:Day)->list[Pill]:
    pills = day.pills
    return pills


def main():
    pill_1 = Pill("Losartan", 50)
    pill_2 = Pill("Atorbastatina", 30)

    day_1 = Day(datetime(2021, 1, 1), [pill_1, pill_2], "First day of the year")
    # day_2 = Day(datetime(2021, 1, 2), pill_atorbasta, "First day of the year")

    print(day_1)


if __name__ == "__main__":
    main()
