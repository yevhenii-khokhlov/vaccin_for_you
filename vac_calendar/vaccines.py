from .intervals import MONTH, YEAR, ZERO

BCG = {
    'name': 'BCG',
    'is_life': True,
    'total': 1,
    'min_intervals': [],
    'standard_calendar': [ZERO],
    'alternative_calendars': [[]],
}

MMR = {
    'name': 'MMR',
    'is_life': True,
    'total': 2,
    'min_intervals': [MONTH],
    'standard_calendar': [YEAR, YEAR*6],
    'alternative_calendars': [[]],
}

HEP_B = {
    'name': 'hep_B',
    'is_life': False,
    'total': 3,
    'min_intervals': [MONTH],
    'standard_calendar': [ZERO, MONTH*2, MONTH*6],
    'alternative_calendars': [[MONTH*2, MONTH*4, MONTH*6]],
}

ROTA = {
    'name': 'rotavirus',
    'is_life': True,
    'total': 2,
    'min_intervals': [MONTH],
    'standard_calendar': [MONTH*2, MONTH*4],
    'alternative_calendars': [[]],
}

DT = {
    'name': 'diphtheria and tetanus',
    'is_life': False,
    'total': 5,
    'min_intervals': [MONTH, MONTH, MONTH, MONTH*6],
    'standard_calendar': [MONTH*2, MONTH*4, MONTH*6, MONTH*18, YEAR*6],
    'alternative_calendars': [[]],
}

PERT = {
    'name': 'pertussis',
    'is_life': False,
    'total': 4,
    'min_intervals': [MONTH, MONTH, MONTH, MONTH*6],
    'standard_calendar': [MONTH*2, MONTH*4, MONTH*6, MONTH*18],
    'alternative_calendars': [[]],
}

POLIO = {
    'name': 'polio',
    'is_life': False,
    'total': 5,
    'min_intervals': [MONTH, MONTH, MONTH, MONTH*6],
    'standard_calendar': [MONTH*2, MONTH*4, MONTH*6, MONTH*18, YEAR*6],
    'alternative_calendars': [[]],
}

HIB = {
    'name': 'hib',
    'is_life': False,
    'total': 3,
    'min_intervals': [MONTH, MONTH*6],
    'standard_calendar': [MONTH*2, MONTH*4, YEAR],
    'alternative_calendars': [[]],
}


def get_vaccines():
    return [BCG, MMR, HEP_B, ROTA, DT, PERT, POLIO, HIB]
