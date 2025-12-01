test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # One or more of the reaction results could be incorrect
          >>> assert np.all(ten_nachos_reactions.get('Reactions') == [
          ...     'Meh.', 'Cheesy!', 'Wow!', 'Wow!', 'Cheesy!',
          ...     'Spicy!', 'Wow!', 'Meh.', 'Cheesy!', 'Wow!'
          ... ])
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
