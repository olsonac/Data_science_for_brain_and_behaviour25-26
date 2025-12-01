
test = {
  'name': 'Question p_gt_0',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'p_gt_0'
          >>> assert 'p_gt_0' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'p_gt_0'
          >>> # from its initial state (of ...)
          >>> assert p_gt_0 is not ...
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # p_gt_0 should be a proportion.
          >>> assert 0 <= p_gt_0 <= 1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Look at the difference values in the notebook.
          >>> # How many are negative or 0?
          >>> assert p_gt_0 == 1
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
