test = {
  'name': 'Question debt_three_years',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'debt_three_years'
          >>> 'debt_three_years' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You have the debt after one year, still.  You need
          >>> # to multiply this value (the debt after one year) by
          >>> # something to get the debt after three years.
          >>> debt_three_years != my_debt * debt_increaser
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You have the debt after two years.  You need
          >>> # to multiply this value (the debt after two years) by
          >>> # something to get the debt after three years.
          >>> debt_three_years != my_debt * debt_increaser * debt_increaser
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Still not quite there.  You need to multiply the calculation
          >>> # of the debt after two years by the debt_increaser variable.
          >>> # The check below allows for tiny differences when you calculate
          >>> # the value in slightly different ways.
          >>> from numpy import isclose
          >>> assert isclose(debt_three_years, my_debt * debt_increaser ** 3)
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
