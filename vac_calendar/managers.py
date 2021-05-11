import datetime

from vac_calendar.vaccines import get_vaccines


class PersonalCalendarManager:
    def __init__(self, date_of_birth: datetime.date, carried_out_vaccinations: dict = None):
        self.carried_out_vaccinations = carried_out_vaccinations
        self.vaccines = get_vaccines()
        self.date_of_birth = date_of_birth

    def get_age(self):
        age = datetime.date.today() - self.date_of_birth
        return age

    def get_next_date(self, interval):
        next_date = self.date_of_birth + interval
        return next_date

    def get_recommended_calendar_for(self, vaccine: dict):
        dates_of_doses_must_given = []
        total_doses = vaccine.get('total')
        standard_calendar = vaccine.get('standard_calendar')

        for i in range(total_doses):
            interval = standard_calendar[i]
            next_dose = self.get_next_date(interval=interval)
            dates_of_doses_must_given.append(next_dose)

        return dates_of_doses_must_given

    def get_recommended_calendar(self):
        recommended_calendar = {}
        for vaccine in self.vaccines:
            name = vaccine.get('name')
            dates = self.get_recommended_calendar_for(vaccine=vaccine)
            recommended_calendar.update({name: dates})
        return recommended_calendar

    def get_calendar(self):
        return self.get_recommended_calendar()
