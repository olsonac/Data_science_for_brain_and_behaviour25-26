test = {
  'name': 'Question outcome_ideal',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'likely_outcome_from_ideal'
          >>> assert 'likely_outcome_from_ideal' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'likely_outcome_from_ideal'
          >>> # from its initial state (of ...)
          >>> assert likely_outcome_from_ideal is not ...
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Value should be from 1 through 5.
          >>> assert 1 <= likely_outcome_from_ideal <= 5
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
