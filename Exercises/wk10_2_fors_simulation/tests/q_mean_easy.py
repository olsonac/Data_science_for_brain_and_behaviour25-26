
test = {
  'name': 'Question mean_easy',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'mean_easy'
          >>> assert 'mean_easy' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'mean_easy'
          >>> # from its initial state (of ...)
          >>> assert mean_easy is not ...
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Ooh - close - but - is the starting value for "total" correct?
          >>> assert mean_easy < 3.7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Not quite there.
          >>> assert 3.6073 < mean_easy < 3.6074
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
