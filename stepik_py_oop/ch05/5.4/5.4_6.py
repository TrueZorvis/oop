class DateError(Exception):
    pass


class DateString:
    def __init__(self, date_string: str):
        self.day, self.month, self.year = self._verify_date(date_string)

    @staticmethod
    def _verify_date(date):
        day, month, year = map(int, date.split('.'))
        if not (1 <= day <= 31) or not (1 <= month <= 12) or not (1 <= year <= 3000):
            raise DateError("Неверный формат даты")
        return day, month, year

    def __str__(self):
        return f"{self.day:02}.{self.month:02}.{self.year}"


date_string = input()
try:
    date = DateString(date_string)
    print(date)
except DateError as e:
    print(e)

print('end')
