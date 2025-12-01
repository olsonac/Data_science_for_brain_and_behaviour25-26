
test = {
  'name': 'Question 1_subtract',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert subtract(5, 10) == -5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert subtract(3, -1) == 4
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
