test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert 2 < number_wow_reactions < 6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Incorrect value for number_wow_reactions
          >>> assert number_wow_reactions == 4
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
