test = {
  'name': 'Question 9_a_median_vs_mean',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'a_median_vs_mean'
          >>> assert 'a_median_vs_mean' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'a_median_vs_mean'
          >>> # from its initial state (of ...)
          >>> assert a_median_vs_mean is not ...
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert np.isclose(a_median_vs_mean, -70.4214)
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
