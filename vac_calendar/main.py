import datetime

from vac_calendar.managers import PersonalCalendarManager
from vac_calendar.table_maker import print_table


if __name__ == '__main__':
    date_of_birth = datetime.date(2020, 12, 11)
    manager = PersonalCalendarManager(date_of_birth=date_of_birth)
    calendar = manager.get_calendar()
    print_table(calendar)
    print(calendar)
