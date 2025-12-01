
test = {
  'name': 'Question 3_1_my_total',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'my_total'
          >>> assert 'my_total' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert my_total == 60
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
