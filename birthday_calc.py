from datetime import datetime, time, timedelta, date


def main():
    yn = 'y'
    while yn == 'y':
        print("Birthday Calculator")
        print()

        name = input("Enter name: ")
        bday = input("Enter birthday (MM/DD/YY): ")

        tday = datetime.today()
        bday = datetime.strptime(bday, "%m/%d/%y")
        difference = tday - bday
        strtday = tday.strftime("%A, %B %-d, %Y")
        strbday = bday.strftime("%A, %B %-d, %Y")
        print("Birthday:", strbday)
        print("Today:", strtday)
        print(name, "is", difference.days, "days old")
        bday = datetime(2020, bday.month, bday.day)
        difference = bday - tday
        if difference.days < 0:
            deff = difference.days * -1
            print(name,"'s birthday was", deff," days ago")
        else:
            print(name,"'s birthday is in", difference.days," days")

        print()
        yn = input("Continue? (y/n):")
        

    

if __name__ == "__main__":
    main()