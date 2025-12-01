
test = {
  'name': 'Question 6_oppose_income',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'oppose_income'
          >>> 'oppose_income' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'oppose_income'
          >>> # from its initial state (of ...)
          >>> oppose_income is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert len(oppose_income) == np.count_nonzero(death == 'Oppose')
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert oppose_income.median() == 29999.5
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
