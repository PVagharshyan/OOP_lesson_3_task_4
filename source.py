import employee

COUNT = 3

def main() -> None:
    list_employees = [employee.Employee() for i in range(COUNT)]
    for item in list_employees:
        item.putdata()
    for item in list_employees:
        item.setdata()
    for item in list_employees:
        item.putdata()


if __name__ == "__main__":
    main()
