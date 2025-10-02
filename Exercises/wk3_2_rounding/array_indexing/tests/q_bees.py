test = {
  'name': 'Question bees',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'bees'
          >>> 'bees' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'bees'
          >>> # from its initial state (of ...)
          >>> bees is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # bees should be an array
          >>> isinstance(bees, np.ndarray)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # bees should be a Boolean array
          >>> bees.dtype == np.dtype(bool)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # There should be four instances of 'be' in the quote.
          >>> np.count_nonzero(bees)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(np.nonzero(bees)[0]) == [1, 5, 7, 11]
          True
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
