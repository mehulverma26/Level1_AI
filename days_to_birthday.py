def bday():
    import datetime
    import sys

    y = 2004
    m = int("05")
    d = 26
    birth = datetime.date(y, m, d)
    today = datetime.date.today()
    if today.day == birth.day and today.month == birth.month:
        print(
            "It is your birthday. Happy birthday!!! \nYou are now",
            today.year - birth.year,
            "years old",
        )
    else:
        if (
            today.month == birth.month
            and today.day >= birth.day
            or today.month > birth.month
        ):
            nextbirthyear = today.year + 1
        else:
            nextbirthyear = today.year
        nextbirthday = datetime.date(nextbirthyear, birth.month, birth.day)
        diff = nextbirthday - today
        print("Days left for your next birthday: ", diff.days)
        print("you will turn :", nextbirthyear - birth.year)


bday()
