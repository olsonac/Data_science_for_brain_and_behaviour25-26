
test = {
  'name': 'Question 8_actual_diff',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'actual_diff'
          >>> assert 'actual_diff' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'actual_diff'
          >>> # from its initial state (of ...)
          >>> assert actual_diff is not ...
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert np.round(actual_diff, 2) == 4535.16
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
