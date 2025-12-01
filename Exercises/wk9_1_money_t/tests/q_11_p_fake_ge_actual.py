
test = {
  'name': 'Question 11_p_fake_ge_actual',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'p_fake_ge_actual'
          >>> assert 'p_fake_ge_actual' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'p_fake_ge_actual'
          >>> # from its initial state (of ...)
          >>> assert p_fake_ge_actual is not ...
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Proportion should be between 0 and 1
          >>> assert 0 <= p_fake_ge_actual <= 1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Proportion should be fairly small
          >>> assert 0 <= p_fake_ge_actual <= 0.06
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
