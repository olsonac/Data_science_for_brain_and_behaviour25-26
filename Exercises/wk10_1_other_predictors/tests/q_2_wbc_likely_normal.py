test = {
  'name': 'Question 2_wbc_likely_normal',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'wbc_likely_normal'
          >>> assert 'wbc_likely_normal' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'wbc_likely_normal'
          >>> # from its initial state (of ...)
          >>> assert wbc_likely_normal is not ...
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert wbc_likely_normal == 3
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
