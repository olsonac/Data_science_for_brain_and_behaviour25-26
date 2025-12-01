
test = {
  'name': 'Question p_props_greater',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'p_props_greater'
          >>> assert 'p_props_greater' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'p_props_greater'
          >>> # from its initial state (of ...)
          >>> assert p_props_greater is not ...
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # p_props_greater should be a proportion.
          >>> assert 0 <= p_props_greater <= 1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The chances are very very low
          >>> assert p_props_greater < 0.00001
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
