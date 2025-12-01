test = {
  'name': 'Question 1_wbc',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'wbc'
          >>> assert 'wbc' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'wbc'
          >>> # from its initial state (of ...)
          >>> assert wbc is not ...
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert np.all(wbc == ckd['White Blood Cell Count'])
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
