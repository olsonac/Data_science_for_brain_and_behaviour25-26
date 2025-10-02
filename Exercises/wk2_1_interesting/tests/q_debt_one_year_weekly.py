test = {
  'name': 'Question debt_one_year_weekly',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'debt_one_year_weekly'
          >>> 'debt_one_year_weekly' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You have the debt after one week.  You need
          >>> # to multiply this value (the debt after one week) by
          >>> # something to get the debt after one year of weekly interest.
          >>> debt_one_year_weekly != my_debt * weekly_debt_increaser
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You have the debt after two weeks.  You need
          >>> # to multiply this value by something to get the debt after one
          >>> # year (52 weeks).
          >>> debt_one_year_weekly != my_debt * weekly_debt_increaser ** 2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Still not quite there.  You should multiply the original
          >>> # debt by the weekly_debt_increaser variable, to the power of 52.
          >>> round(debt_one_year_weekly, 4) == 551.4928
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
