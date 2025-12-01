test = {
  'name': 'Question p_males_gte',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'p_males_gte'
          >>> assert 'p_males_gte' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'p_males_gte'
          >>> # from its initial state (of ...)
          >>> assert p_males_gte is not ...
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # p_males_gte should be a proportion
          >>> assert 0 <= p_males_gte <= 1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The proportion will be small
          >>> assert 0 <= p_males_gte <= 0.001
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Really small
          >>> assert 0 <= p_males_gte <= 0.00001
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
