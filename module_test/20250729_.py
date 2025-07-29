import datetime
birth_month, birth_day=input("생일입력: mm/dd>>>>> ").split("/")
print(birth_month,birth_day)

today=datetime.date.today()

birthday_this_year=datetime.date(today.year, int(birth_month), int(birth_day))

if today>birthday_this_year:
    birth_next=datetime.date(today.year+1,int(birth_month),int(birth_day))
else:
    birth_next=birthday_this_year

days_left=(birth_next-today).days
print(days_left,"일 남았다")