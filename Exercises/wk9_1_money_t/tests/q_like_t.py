test = {
  'name': 'Question like_t',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'like_t'
          >>> assert 'like_t' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'like_t'
          >>> # from its initial state (of ...)
          >>> assert like_t is not ...
          """,
          'hidden': False,
          'locked': False
        },
        {
          # See simulate_like_t.py for limits.
          'code': r"""
          >>> assert 1.74 < like_t < 1.85
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
