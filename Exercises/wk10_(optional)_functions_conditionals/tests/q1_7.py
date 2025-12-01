test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert nacho_result in ['Wow!', 'Meh.', 'Okay!']
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ten_nachos = np.array(['neither', 'cheese', 'both', 'both',
          ...                        'cheese', 'salsa', 'both', 'neither',
          ...                        'cheese', 'both'])
          >>> ten_nachos_reactions = pd.DataFrame()
          >>> ten_nachos_reactions['Nachos'] = ten_nachos
          >>> ten_nachos_reactions['Reactions'] = ten_nachos_reactions['Nachos'].apply(nacho_reaction)
          >>> assert both_or_neither(ten_nachos_reactions) == 'Wow!'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> seven_nachos = np.array(['neither', 'cheese', 'both', 'both',
          ...                          'neither', 'both', 'neither'])
          >>> seven_nachos_reactions = pd.DataFrame()
          >>> seven_nachos_reactions['Nachos'] = seven_nachos
          >>> seven_nachos_reactions['Reactions'] = seven_nachos_reactions['Nachos'].apply(nacho_reaction)
          >>> assert both_or_neither(seven_nachos_reactions) == 'Okay!'
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
