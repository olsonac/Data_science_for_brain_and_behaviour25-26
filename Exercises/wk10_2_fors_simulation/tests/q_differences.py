
test = {
  'name': 'Question differences',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to make a column called 'Difference'
          >>> assert 'Difference' in list(christenings)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The first two values should be 532 and 401
          >>> assert christenings.loc[0, 'Difference'] == 535
          >>> assert christenings.loc[1, 'Difference'] == 401
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Nearly there ..
          >>> assert np.sum(christenings['Difference']) == 30224
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
