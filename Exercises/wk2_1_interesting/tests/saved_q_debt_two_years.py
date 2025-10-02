test = {
  'name': 'Question debt_two_years',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'debt_two_years'
          >>> 'debt_two_years' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You have the debt after one year, still.  You need
          >>> # to multiply this value (the debt after one year) by
          >>> # something to get the debt after two years.
          >>> debt_two_years != my_debt * debt_increaser
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Still not quite there.  You need to multiply the calculation
          >>> # of the debt after one year by the debt_increaser variable.
          >>> # The check below allows for tiny differences when you calculate
          >>> # the value in slightly different ways.
          >>> from numpy import isclose
          >>> assert isclose(debt_two_years,
          ...         my_debt * debt_increaser * debt_increaser)
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
