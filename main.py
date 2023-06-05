from pill import Pill


def main():
    pill = Pill("Losartan", 50)
    print(pill)
    pill.change_name("Atorbastatina")
    print(pill)


if __name__ == "__main__":
    main()
