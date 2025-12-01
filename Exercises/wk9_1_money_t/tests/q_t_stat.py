test = {
  'name': 'Question t_stat',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 't_stat'
          >>> assert 't_stat' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 't_stat'
          >>> # from its initial state (of ...)
          >>> assert t_stat is not ...
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # t_stat should be just the statistic value, not the
          >>> # full results structure that comes back from the Scipy
          >>> # t-test.  See the textbook page for details.
          >>> assert not hasattr(t_stat, 'statistic')
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert np.isclose(t_stat, 1.788676747081)
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
