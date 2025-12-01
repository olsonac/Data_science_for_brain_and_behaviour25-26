test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert spicy_nacho == 'Spicy!'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert nacho_reaction('cheese') == 'Cheesy!'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert nacho_reaction('both') == 'Wow!'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert nacho_reaction('neither') == 'Meh.'
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
