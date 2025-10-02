test = {
  'name': 'Question debt_ten_years',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'debt_ten_years'
          >>> 'debt_ten_years' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You have the debt after one year, still.  You need
          >>> # to multiply this value (the debt after one year) by
          >>> # something to get the debt after ten years.
          >>> debt_ten_years != my_debt * debt_increaser
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You have the debt after two years.  You need
          >>> # to multiply this value  by something to get the debt after ten
          >>> # years.
          >>> debt_ten_years != my_debt * debt_increaser * debt_increaser
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Still not quite there.  You should multiply the original
          >>> # debt by the debt_increaser variable, to the power of 10
          >>> round(debt_ten_years, 4) == 1296.8712
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
